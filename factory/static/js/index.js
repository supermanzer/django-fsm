/**
index.js
--------------------------------------------------------------
Custom javascript functions and constants for the Factory applciation.
*/
/*
    Constants
-------------------------------------------------------------
*/
const modelels = {
    window: '#matmodal',
    content: '#modal-content'
};

/*
Materialize Component Initialization Functions
-------------------------------------------------------------
*/
function indexInit() {
    // Initializing our sidenav
    var elems = document.querySelectorAll('.sidenav');
    var options = {};
    var insts = M.Sidenav.init(elems,{});
    // Initializing a general modal
    var elems = document.querySelectorAll(".modal");
    var options = {}
    var insts = M.Modal.init(elems, options);
}
// Initializing some basic form elements - Adjust options to change behavior
function formInit(){
    // Initializing any datepickers
    var elems = document.querySelectorAll('.datepicker');
    var options = {format:'yyyy-mm-dd'};
    var insts = M.Datepicker.init(elems);
    // Initializing any timepickers
    var elems = document.querySelectorAll('.timepicker');
    var options = {};
    var insts = M.Timepicker.init(elems);
    // Initializing Select elements
    var elems = document.querySelectorAll('select');
    var options = {};
    var insts = M.FormSelect.init(elems, options);
}



/*
    Action Binding and General Functions
-------------------------------------------------------------
*/
function assignNewWidget() {
    var elem = document.querySelector('.js-new-widget');
    elem.addEventListener('click', function(event){
        event.preventDefault();
        var mW = document.querySelector(modelels.window);
        var mC = document.querySelector(modelels.content);
        var resp = fetch(elem.dataset.url)
                    .then(resp=>resp.json())
                    .then(response =>{
                        if (response.is_valid) {
                            mC.innerHTML = response.html
                        } else {
                            mC.innerHTML = response.err_msg
                        }
                        M.Modal.getInstance(mW).open()
                    }).then(response => {
                        formInit()
                    }).then(resp => {
                        el = document.querySelector('form.js-make-widget')
                        el.addEventListener('submit', createWidget)
                    })
    });
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

function createWidget(event) {
    event.preventDefault();
    var form = document.querySelector('form.js-make-widget');
    var fD = new FormData(form);
    var reload_target = form.dataset.reload;
    var url = form.getAttribute('action')
    var resp = fetch(url, {
        method: 'POST',
        body: fD,
        credentials: 'same-origin'
    })
        .then(resp=>resp.json())
        .then(myJson => {
            var el = document.querySelector(reload_target)
            if (myJson.is_valid) {
                el.innerHTML = myJson.html;
            } else {
                el.innerHTML = myJson.err_msg;
            }
        });
    M.Modal.getInstance(document.querySelector('#matmodal')).close();
}
/*
 Generic Form Handling Functions
 ------------------------------------------------------------
 */
 // This function returns an array of objects for each input
 function serializeArray(form) {
	    var field, l, s = [];
	    if (typeof form == 'object' && form.nodeName == "FORM") {
	        var len = form.elements.length;
	        for (var i=0; i<len; i++) {
	            field = form.elements[i];
	            if (field.name && !field.disabled && field.type != 'file' && field.type != 'reset' && field.type != 'submit' && field.type != 'button') {
	                if (field.type == 'select-multiple') {
	                    l = form.elements[i].options.length;
	                    for (j=0; j<l; j++) {
	                        if(field.options[j].selected)
	                            s[s.length] = { name: field.name, value: field.options[j].value };
	                    }
	                } else if ((field.type != 'checkbox' && field.type != 'radio') || field.checked) {
	                    s[s.length] = { name: field.name, value: field.value };
	                }
	            }
	        }
	    }
	    return s;
	}
