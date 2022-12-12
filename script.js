function age_cheker(){
    let cookies_list = document.cookie.split(";")
    for (let i = 0; i < cookies_list.length; i++){

        let [name, value] = cookies_list[i].split("=");
        if ((name.trim() == "age_cheker") && (value.trim() == "true")){
            return true
        } 
    }
    return false
};

function confirm_age(){
    console.log(document.cookie)
    if (age_cheker()){
        let head = document.querySelectorAll('.disable');
        for (let el of head) {
            el.classList.remove("disable");
        }
        let checker = document.querySelector(".age-checker")
        checker.classList.add("not-visible");
    } else {
        var btn_confirm = document.getElementById("confirm-age");
        btn_confirm.onclick = function() {
            let head = document.querySelectorAll('.disable');
            for (let el of head) {
                el.classList.remove("disable");
            }
            let checker = document.querySelector(".age-checker")
            checker.classList.add("not-visible");
            document.cookie = "age_cheker=true"
        } 
    
        var not_btn_confirm = document.getElementById("not-confirm-age");
        not_btn_confirm.onclick = function() {
            if (!document.querySelector(".refusal")){
                let div = document.createElement('div');
                div.classList.add("refusal")
                div.innerHTML = "<p class='warning'><b>Данный сайт не доступен для вас.</b></p>"
                content = document.querySelector(".content-popup")
                content.append(div)
            }
        }
    };
}

confirm_age();