window.addEventListener("DOMContentLoaded", () => {

        const memorySidebar =
        document.querySelector(
      ".memory-sidebar"
    );

    const memoryToggle =
        document.getElementById(
    "memoryToggle"
    );

    const overlay =
        document.getElementById(
    "sidebarOverlay"
    );


    console.log(
    "MEMORY SIDEBAR:",
    memorySidebar
    );

    console.log(
    "MEMORY TOGGLE:",
    memoryToggle
    );

    console.log(
    "OVERLAY:",
    overlay
    );



    function closeMemory(){

    memorySidebar.classList.remove(
        "open"
    );

    overlay.classList.remove(
        "show"
    );

    memoryToggle.classList.remove(
        "hidden"
    );

}


    function toggleMemory(){

    memorySidebar.classList.add(
        "open"
    );

    overlay.classList.add(
        "show"
    );

    memoryToggle.classList.add(
        "hidden"
    );
}

    memoryToggle.addEventListener(
    "click",
    toggleMemory
    );


    overlay.addEventListener(
    "click",
    closeMemory
);



    loadMemoryData()
    .catch(error => {

        console.error(
            "MEMORY LOAD ERROR:",
        error
        );

});

    
    const btn = document.getElementById("analyzeBtn");
    const statusRing =
    document.querySelector(
        ".status-ring"
    );

    const result = document.getElementById("result");
    const journalText = document.getElementById("journalText");

    const statusText =
    document.getElementById(
        "statusText"
    );

    console.log("Button:", btn);
    console.log("Result:", result);




    async function loadMemoryData(){

    try {

        const userId =
        localStorage.getItem(
            "user_id"
        );

        console.log(
            "MEMORY USER:",
            userId
        );

        if (!userId){

            console.log(
                "NO USER ID FOUND"
            );

            return;
        }

        const response =
        await fetch(
            `http://127.0.0.1:5000/memory-data?user_id=${userId}`
        );

        const data =
        await response.json();
        document.getElementById(
            "checkinCount"
        ).textContent =
        data.checkins;

        const memoryList =
        document.getElementById(
            "memoryList"
        );

        memoryList.innerHTML = "";

        data.memories.forEach(
            memory => {

                memoryList.innerHTML += `
                    <div class="memory-card">
                        ${memory.memory_content}
                    </div>
                `;
            }
        );

    }

    catch(error){

        console.error(
            "MEMORY ERROR:",
            error
        );
    }
}

    btn.addEventListener("click", async () => {

        try {

            const text = journalText.value.trim();

             console.log(
                "TEXT:",
            text
            );

            if (!text) {
                alert("Please enter something first.");
                return;
            }


            console.log(
            "BEFORE FETCH"
            );

            console.log(
                "STATUS TEXT:",
             statusText
        );  

            console.log(
            "STATUS RING:",
                statusRing
        );

            statusText.textContent =
            "Reflecting...";

            statusRing.className =
            "status-ring reflecting";
            const response = await fetch(
    "http://127.0.0.1:5000/analyze-stream",
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            text: text,
            user_id: localStorage.getItem("user_id")
            })
        }
    );

    console.log(
            "AFTER FETCH"
    );

if (!response.ok) {
    throw new Error(`Server Error: ${response.status}`);
}

const userBubble =
document.createElement("div");

userBubble.className =
"user-message";

userBubble.textContent =
text;

result.appendChild(
    userBubble
);

result.parentElement.scrollTop =
    result.parentElement.scrollHeight;

const anchaBubble =
document.createElement("div");

anchaBubble.className =
"ancha-message";

anchaBubble.innerHTML = `
    <div class="typing-indicator">
        <span></span>
        <span></span>
        <span></span>
    </div>
`;

result.appendChild(
    anchaBubble
);

statusText.textContent =
"Typing...";

statusRing.className =
"status-ring typing";

const reader =
response.body.getReader();

console.log(
    "READER CREATED"
);

const decoder =
new TextDecoder();


let firstChunk = true;

while (true) {

    const {
        done,
        value
    } = await reader.read();

    if (done) break;

    const chunk =
        decoder.decode(value);

    console.log(
    "CHUNK:",
    chunk
    );

    if (firstChunk){

    anchaBubble.innerHTML = "";

    firstChunk = false;
}

    anchaBubble.textContent +=
        chunk;

    result.parentElement.scrollTop =
    result.parentElement.scrollHeight;
}
    statusText.textContent =
    "Listening...";

    statusRing.className =
    "status-ring listening";

    journalText.value = "";
    

    }

        catch (error) {

        console.error(
            "FRONTEND ERROR:",
            error
        );

        statusRing.className =
        "status-ring listening";
    }

    });

});