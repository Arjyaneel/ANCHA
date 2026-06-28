document
.getElementById("loginBtn")
.addEventListener("click", async () => {

    const username =
        document.getElementById("username").value;

    const password =
        document.getElementById("password").value;

    const response =
        await fetch(
            "http://127.0.0.1:5000/login",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                    "application/json"
                },

                body: JSON.stringify({
                    username,
                    password
                })
            }
        );

    const data =
        await response.json();

    if (!response.ok) {

        alert(data.error);

        return;
    }

    localStorage.setItem(
        "user_id",
        data.user_id
    );

    localStorage.setItem(
        "username",
        data.username
    );

    window.location.href =
        "index.html";
});