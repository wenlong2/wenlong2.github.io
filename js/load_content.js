function show_content(url) {
    var xhr = new XMLHttpRequest();
    xhr.onload = function () {
        document.getElementById('main_body').innerHTML = this.responseText;
    };
    xhr.open('GET', url);
    xhr.send();
}
function go_home() {
    show_content('content/home.html')
}
function go_research() {
    show_content('content/research.html')
}
function go_cv() {
    show_content('content/cv.html')
}
function go_tools() {
    show_content('content/tools.html')
}
function go_contact() {
    show_content('content/contact.html')
}

go_home()

