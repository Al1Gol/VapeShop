var btn_confirm = document.getElementById("confirm-age");
btn_confirm.onclick = function() {
	let head = document.querySelectorAll('.disable');
    for (let el of head) {
        el.classList.remove("disable");
    }
    let checker = document.querySelector(".age-checker")
    checker.classList.add("not-visible");
};

var not_btn_confirm = document.getElementById("not-confirm-age");
not_btn_confirm.onclick = function() {
    if (!document.querySelector(".refusal")){
        let div = document.createElement('div');
        div.classList.add("refusal")
        div.innerHTML = "<p class='warning'><b>Данный сайт не доступен для вас.</b></p>"
        content = document.querySelector(".content-popup")
        content.append(div)
    }
};
