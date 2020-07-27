function show_content(url, eid='main_body') {
    var xhr = new XMLHttpRequest();
    xhr.onload = function () {
        document.getElementById(eid).innerHTML = this.responseText;
    };
    xhr.open('GET', url);
    xhr.send();
    document.getElementById(eid).contentWindow.location.reload();
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
function show_side_bar() {
    show_content('content/sidebar.html', eid='side_bar')
}

go_home()

show_side_bar()
