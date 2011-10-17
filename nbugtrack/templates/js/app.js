/* XXX: My JavaScript is pretty bad: gotta clean it up :( */
already_open = false

function new_project() {   
    if (!already_open) {
	already_open = true;

	var existing_view = $("#proj_listing ol").html();
	var textinput = '<li><div id="project_data"><div class="proj_name"><input id="project_input" type="text" placeholder="new project name">' + '</input>';
	var textarea = '<textarea rows="5" cols="50" id="project_description" placeholder="project description" wrap="soft">' + '</textarea>';
	var button = '<input type="button" value="Save" class="saveButton" /> <input type="button" value="Cancel" class="cancelButton"/></div></div></li>';

	$("#proj_listing ol").html(existing_view + textinput +"<br /><br />"+ textarea + "<br /><br />" + ' ' + button);
	$('.saveButton').click(function() {saveProjectChanges();});
	$('.cancelButton').click(function() {	
	$("#proj_listing ol").html(existing_view);
	    already_open = false;
	});			   
	$('#project_input').focus();
    }
}

function saveProjectChanges() {
    var new_proj_name = document.getElementById("project_input").value;
    var new_proj_desc = document.getElementById("project_description").value;
    
    if(new_proj_name != "") {
	if(new_proj_desc != "") {
    already_open = false;
    $.post("/new_project", {name: new_proj_name, desc: new_proj_desc}, 
	   function() {
	       window.location.reload();
	   });
	}
	else {
	    $("#project_description").css('border','1px solid red');
	}
    }
    else {
	$("#project_input").css('border','1px solid red');
    }
}

function rename_project() {
    if (!already_open) {
	already_open = true;

	var existing_html = $("header").html()
	var textinput = '<input id="rename_input" type="text" placeholder="new project name">' + '</input>';
	var button = '<input type="button" value="Save" class="saveButton" /> <input type="button" value="Cancel" class="cancelButton"/></div></div></li>';

	$("header").html(existing_html + "<br />" + textinput +" "+ ' ' + button);
	$('.saveButton').click(function() {saveRenameChanges();});
	$('.cancelButton').click(function() {	
	$("header").html(existing_html);
	    already_open = false;
	});			   
	$('#rename_input').focus();
    }    
}

function saveRenameChanges() {
    var new_proj_name = document.getElementById("rename_input").value;
    var existing_name = $("#rename_trigger").text().trim();

    if(new_proj_name != "") {
	already_open = false;
	$.post("/rename_project", {oldname: existing_name, newname: new_proj_name}, 
	   function() {
	       window.location.href = "../"+new_proj_name;
	   });
    } else {
    	$("#rename_input").css('border','1px solid red');
    }
}

function update_project() {
    if (!already_open) {
	already_open = true;

	var existing_text = $('update_trigger').text();
	var existing_view = $("#project_description").html();
	var textarea = '<textarea rows="5" cols="50" id="update_input" wrap="soft">' + '</textarea>';
	var button = '<input type="button" value="Save" class="saveButton" /> <input type="button" value="Cancel" class="cancelButton"/>';

	$("#project_description").html(existing_view + "<br/><br />"+ textarea + "<br /><br />" + ' ' + button);
	$('.saveButton').click(function() {saveUpdateChanges();});
	$('.cancelButton').click(function() {	
	$("#project_description").html(existing_view);
	    already_open = false;
	});			   
	$('#update_input').focus();
    }
}

function saveUpdateChanges() {
    var new_proj_desc = document.getElementById("update_input").value;
    var existing_name = $("#rename_trigger").text().trim();

    if(new_proj_desc != "") {
    already_open = false;
    $.post("/update_project", {name: existing_name, desc: new_proj_desc}, 
	   function() {
	       window.location.reload();
	   });
    } else {
	$("#update_input").css('border','1px solid red');
    }
}

function delete_project() {
    delete_it =  confirm("Delete: Sure? I'm not kidding!\nAll the bugs, wiki with that project will be gone too!");
    
    if(delete_it) {
	$.get("/delete_project?name="+$("#rename_trigger").text().trim(), 
	      function(data) {
		  window.location.href = "../";
	      });
    }
}

function new_bug() {
}
    
function new_wiki() {
}

function update_wiki() {
}

function update_bug() {
}

$(document).ready(function(){
});
