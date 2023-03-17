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
        let head = document.querySelector('header')
        head.classList.add("disable");
        let content = document.querySelector('div.content')
        content.classList.add("disable");
        let footer = document.querySelector('footer')
        footer.classList.add("disable");
        let div = document.createElement('div');
        div.classList.add("age-checker");
        document.body.append(div);
        let div_header = document.createElement('div');
        div_header.classList.add("header-popup", "text-white-50", "bg-dark");
        div_header.innerHTML = '<h4>Предупреждение!!!</h4>';
        div.append(div_header);
        let div_body = document.createElement('div');
        div_body.classList.add("content-popup");
        div_body.innerHTML = '<h3>Данный сайт предназначен для лиц старше 18 лет.</h3>';
        div.append(div_body);
        let btns = document.createElement('div');
        btns.classList.add("checher-age");
        div_body.append(btns);
        let btn_yes = document.createElement('button');
        let btn_no = document.createElement('button');
        btn_yes.classList.add("popup-btn", "text-white-50", "bg-dark");
        btn_no.classList.add("popup-btn", "text-white-50", "bg-dark");
        btn_yes.id = 'confirm-age'
        btn_no.id = 'not-confirm-age'
        btn_yes.innerText = 'Мне есть 18 лет'
        btn_no.innerText = 'Мне нет 18 лет'
        btns.append(btn_yes);
        btns.append(btn_no);




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