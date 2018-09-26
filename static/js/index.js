/**
index.js
--------------------------------------------------------------
Custom javascript functions and constants for the Factory applciation.
*/
const modelels = {
    window: '#matmodal',
    content: '#modal-content'
};

function assignNewWidget() {
    var elem = document.querySelector('.js-new-widget');
    var mW = document.querySelector(modelels.window);
    var mC = document.querySelector(modelels.content);
    elem.addEventListener('click', function(){
        var resp = fetch(elem.dataset.url)
                    .then(resp=>resp.json())
                    .then(response =>{
                        if (response.is_valid) {
                            mC.innerHTML = response.html
                        } else {
                            mC.innerHTML = response.err_msg
                        }
                        M.Modal.getInstance(mW).open()
                    });
    });
}

function indexInit() {
    // Initializing our sidenav
    var elems = document.querySelectorAll('.sidenav');
    var options = {};
    var insts = M.Sidenav.init(elems,{});
    // Initializing a general modal
    var elems = document.querySelectorAll(".modal");
    var options = {}
    var insts = M.Modal.init(elems, options)
}

function loadWidgets() {
    var div = document.querySelector('.js-load-widgets');
    var resp = fetch(div.dataset.url)
                .then(resp=>resp.json())
                .then(myJson => {
                    if (myJson.is_valid) {
                        div.innerHTML = myJson.html
                    } else {
                        div.innerHTML = myJson.err_msg
                    }
                }).then(response => {
                    assignNewWidget()
                });
    return resp
}
