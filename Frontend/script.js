window.addEventListener("DOMContentLoaded", () => {

    const btn = document.getElementById("analyzeBtn");
    const result = document.getElementById("result");
    const journalText = document.getElementById("journalText");

    console.log("Button:", btn);
    console.log("Result:", result);

    const emotionIcons = {
        happy: "😊",
        excited: "🎉",
        stressed: "🌧️",
        sad: "🍂",
        anxious: "🌊",
        calm: "🌿",
        attached: "💛",
        tired: "😴",
        lazy: "🛋️"
    };

    btn.addEventListener("click", async () => {

        try {

            const text = journalText.value.trim();

            if (!text) {
                alert("Please enter something first.");
                return;
            }

            result.innerHTML = `
                <div class="ancha-message">
                    <p>Analyzing your emotions...</p>
                </div>
            `;

            const response = await fetch(
                "http://127.0.0.1:5000/analyze",
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

if (!response.ok) {
    throw new Error(`Server Error: ${response.status}`);
}

            const data = await response.json();

            
            console.log("Energy =", data.energy_level);
            console.log("Tips =", data.tips);

alert(JSON.stringify(data, null, 2));;

            result.innerHTML = `
                <div class="user-message">
                    ${text}
                </div>

                <div class="ancha-message">

                    <div class="mood-chips">

                        <span class="chip emotion-chip">
                            ${emotionIcons[data.emotion] || "💭"}
                            ${data.emotion || "unknown"}
                        </span>

                        <span class="chip energy-chip">
                            ⚡
                            ${data.energy_level || "unknown"}
                        </span>

                    </div>

                    <div class="response-text">

                        <p>
                            ${data.mood_summary || ""}
                        </p>

                        <br>

                        <p>
                            ${data.support_response || ""}
                        </p>

                    </div>

                    <div class="tips-card">

                        <h3>Today's Ingredients</h3>

                        <ul>

                            ${
                                Array.isArray(data.tips)
                                ? data.tips
                                    .map(tip => `<li>${tip}</li>`)
                                    .join("")
                                : `<li>${data.tips || "No tips available"}</li>`
                            }

                        </ul>

                    </div>

                </div>
            `;

            journalText.value = "";

        }
        catch (error) {

            console.error("FRONTEND ERROR:", error);

            result.innerHTML = `
                <div class="ancha-message">
                    <p>
                        Something went wrong.
                        Check browser console.
                    </p>
                </div>
            `;
        }

    });

});

