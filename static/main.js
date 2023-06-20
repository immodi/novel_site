const novelsNames = document.querySelectorAll(".novel-name")

novelsNames.forEach(name => {
    if (name.innerHTML.length < 40) {
        return
    } else {
        name.innerHTML = name.innerHTML.slice(0, 39) + "..."
    }
});