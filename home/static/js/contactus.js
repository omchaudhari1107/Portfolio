
function PostData() {
    const form = document.getElementById("form");
    const msg = document.getElementById("msg");
    msg.style.display = "none";
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const num = document.getElementById("number").value;
    const comment = document.getElementById("comment").value;
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const data = email
    if (!emailRegex.test(email)) {
        alert("Please enter a valid email address.");
        return;
    }

    if (!name || !email || !num || !comment) {
        alert("Please fill in all fields.");
        return 0;
    }

    if (num.length > 10 || isNaN(num)) {
        alert("Invalid contact number.");
        document.getElementById("number").value = "";
        return 0;
    }

    try {
        form.action = "https://sheetdb.io/api/v1/grk5segswznim";
        form.addEventListener("submit", (e) => {
            e.preventDefault();
            fetch(form.action, {
                method: "post",
                body: new FormData(form),
            })
            .then(() => {
                msg.style.display = "block";
                msg.style.color = "greenyellow";
                msg.style.fontWeight = "bold";
                msg.style.fontSize = "large";
                msg.style.textAlign = "center";
                msg.style.fontFamily = "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif";
                msg.innerHTML = "Thanks for contacting me!";
                form.reset();
            })
            .then((html) => {
                // window.open("index.html", "_self");
            });
        });
    } catch (error) {
        alert(error);
    }
}
