javascript:(function(){
    document.querySelectorAll(".product").forEach(product => {
        let name = product.querySelector(".product-title")?.innerText.toLowerCase();
        let gender = product.querySelector(".gender")?.innerText.toLowerCase();
        let conflict = "";

        if (name && gender) {
            if (name.includes("men") && gender !== "male" && gender !== "men") {
                conflict = `⚠ Conflict: Men’s product marked as '${gender}'`;
            }
            if (name.includes("women") && gender !== "female" && gender !== "women") {
                conflict = `⚠ Conflict: Women’s product marked as '${gender}'`;
            }
        }

        if (conflict) {
            product.style.border = "2px solid red"; // Highlight in red
            product.title = conflict; // Show conflict details on hover
        }
    });
})();
