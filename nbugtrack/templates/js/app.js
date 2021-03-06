/* XXX: My JavaScript is pretty bad: gotta learn it properly.. :( */
/* Much of the following code is pretty similar... */
already_open = false;
invalid_chars = /[\#\$\@\!\^\&\*]+/;

function enable_hotkeys() {
    shortcut.add("w",new_wiki, {'type':'keydown','target':document, 'disable_in_input':true});
    shortcut.add("b",new_bug,{'type':'keydown','target':document, 'disable_in_input':true});
    shortcut.add("n",new_project,{'type':'keydown','target':document, 'disable_in_input':true});
}

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
    
    if(new_proj_name != "" && !new_proj_name.match(invalid_chars)) {
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
    var existing_name = $.trim($("#rename_trigger").text());

    if(new_proj_name != "" && !new_proj_name.match(invalid_chars)) {
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
    var existing_name = $.trim($("#rename_trigger").text());

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
    
    if(delete_it) { /* trim() is not supported in IE 8 !!*/
	$.get("/delete_project?name=" + $.trim($("#rename_trigger").text()), 
	      function(data) {
		  window.location.href = "../";
	      });
    }
}
    
function new_wiki() {
    if (!already_open) {
	already_open = true;
	var existing_html = $("#wiki_data .list_wiki").html();
    
	var textField = '<li><input type="text" placeholder="New WikiPage Name" id="wiki_input"></input>';
	var button = '<input type="button" value="Save" class="saveButton" /> <input type="button" value="Cancel" class="cancelButton"/></li>';

	$("#wiki_data .list_wiki").html(existing_html + textField +" "+ button);
	$('.saveButton').click(function() {saveNewWiki();});
	$('.cancelButton').click(function() {	
	    $("#wiki_data .list_wiki").html(existing_html);
	    already_open = false;
	});			   
	$('#wiki_input').focus();
    }    
}

function saveNewWiki() {
    var wiki_name = document.getElementById("wiki_input").value;
    var proj_name = $("#rename_trigger").text();

    if(wiki_name != "") {
	already_open = false;
	$.post("/new_wiki", {project_name: proj_name, name: wiki_name, content: "Wiki content for "+wiki_name}, 
	       function() {
		   window.location.reload();
	       });
    } else {
	$("#wiki_input").css('border','1px solid red');
    }
}

/* XXX */
function new_bug() {
    if (!already_open) {
	already_open = true;

	var existing_html = $("#bugs_data").html();    
	var textField = '<input type="text" placeholder="Bug Title" id="bug_input"></input>';
	var button = '<input type="button" value="Save" class="saveButton" /> <input type="button" value="Cancel" class="cancelButton"/>';

	$("#bugs_data").html(existing_html + textField + " " + button);
	$('.saveButton').click(function() {saveNewBug();});
	$('.cancelButton').click(function() {	
	    $("#bugs_data").html(existing_html);
	    already_open = false;
	});			   
	$('#bug_input').focus();
    }    
}

function saveNewBug() {
    var bug_name = document.getElementById("bug_input").value;
    var proj_name = $("#rename_trigger").text();

    if(bug_name != "") {
	already_open = false;
	$.post("/new_bug", {project_name: proj_name, shortname: bug_name},
	       function() {
		   window.location.reload();
	       });
    } else {
	$("#bug_input").css('border','1px solid red');
    }
}

function rename_wiki() {
    if (!already_open) {
	already_open = true;

	var existing_html = $("header").html()
	var textinput = '<input id="rename_input" type="text" placeholder="new wiki name">' + '</input>';
	var button = '<input type="button" value="Save" class="saveButton" /> <input type="button" value="Cancel" class="cancelButton"/></div></div></li>';

	$("header").html(existing_html + "<br />" + textinput +" "+ ' ' + button);
	$('.saveButton').click(function() {saveWikiRenameChanges();});
	$('.cancelButton').click(function() {	
	$("header").html(existing_html);
	    already_open = false;
	});			   
	$('#rename_input').focus();
    }    
}

function saveWikiRenameChanges() {
    var new_wiki_name = document.getElementById("rename_input").value;
    var existing_name = $.trim($("#rename_trigger").text());

    if(new_wiki_name != "") {
	already_open = false;
	$.post("/rename_wiki", {wiki_id: $("#pageid").text(), newname: new_wiki_name}, 
	   function() {
	       window.location.reload();
	   });
    } else {
    	$("#rename_input").css('border','1px solid red');
    }
}

function update_wiki() {
    already_open = true;
    var existing_content =  $('#wiki_content').html();
    var inplace_text = ""
    $.post("/send_wtext", {id: $.trim($('#pageid').text())}, 
	  function(data) {
	      inplace_text = data;
	      $('#wiki_input').html(inplace_text);
	  }, "text");
    var textinput = '<textarea id="wiki_input" rows="10" cols="60"></textarea>';
    var button = '<input type="button" value="Save" class="saveButton" /> <input type="button" value="Cancel" class="cancelButton"/></div></div></li>';

    $('#wiki_content').html(textinput+'<br />'+button);
    $('.saveButton').click(function() {saveWikiUpdateChanges();});
    $('.cancelButton').click(function() {	
	$("#wiki_content").html(existing_content);
	already_open = false;
    });			   
    $('#wiki_input').focus();
}

function saveWikiUpdateChanges()
{
    var new_wiki_content = document.getElementById("wiki_input").value;
    
    if(new_wiki_content != "") {
	already_open = false;
	$.post("/update_wiki", {id: $("#pageid").text(), content: new_wiki_content}, 
	   function() {
	       window.location.reload();
	   });
    } else {
    	$("#rename_input").css('border','1px solid red');
    }
}

function update_bug() {
    already_open = true;
    var eheader, ebug_status, stat_input, ebug_prio, prio_input, ebug_desc, desc_input;
    eheader = $("header").html();
    ebug_stat = $("#bug_stat").html();
    ebug_prio = $("#bug_prio").html();
    stat_input = '<input type="text" placeholder="'+ebug_stat+'" id="stat_input"> </input>';
    prio_input = '<input type="text" placeholder="'+ebug_prio+'" id="prio_input"> </input>';
    console.log(stat_input);
    console.log(prio_input);
    ebug_desc = $("#bug_desc").html();
    desc_input = '<textarea id="desc_input" rows="10" cols="60"></textarea></textarea>'
    var button = '<input type="button" value="Save Changes" class="saveButton" /> <input type="button" value="Revert Back" class="cancelButton"/></div></div></li>';

    var inplace_text = ""

    $.post("/send_btext", {id: $.trim($('#bugid').text())}, 
	   function(data) {
	       inplace_text = data;
	       $('#desc_input').html(inplace_text);
	   }, "text");
    
    $('#bug_stat').html(stat_input);
    $('#bug_prio').html(prio_input);
    $('#bug_desc').html(desc_input);
    $('header').html(eheader + "<br /> <br />"+ button);
    $('.saveButton').click(function() {saveBugUpdateChanges(ebug_stat, ebug_prio, ebug_desc, eheader);});
    $('.cancelButton').click(function() {	
	$('#bug_stat').html(ebug_stat);
	$('#bug_prio').html(ebug_prio);
	$('#bug_desc').html(ebug_desc);
	$('header').html(eheader);
	already_open = false;
    });			   
    $('#desc_input').focus();
}

function saveBugUpdateChanges(ebug_stat, ebug_prio, ebug_desc, eheader)
{
    var new_bug_stat = document.getElementById("stat_input").value;
    var new_bug_prio = document.getElementById("prio_input").value;
    var new_bug_desc = document.getElementById("desc_input").value;

    if (new_bug_stat == "") new_bug_stat = ebug_stat;
    if (new_bug_prio == "") new_bug_prio = ebug_prio;

    if(new_bug_desc !== ebug_desc || new_bug_stat !== ebug_stat || new_bug_prio !== ebug_prio) {     // if one of them is changed
	already_open = false;
	$.post("/update_bug", {id: $("#bugid").text(), desc: new_bug_desc, prio: new_bug_prio, stat: new_bug_stat}, 
	   function() {
	       window.location.reload();
	   });
    } else {       // I'll just reset the state
	$('#bug_stat').html(ebug_stat);
	$('#bug_prio').html(ebug_prio);
	$('#bug_desc').html(ebug_desc);
	$('header').html(eheader);
	already_open = false; 
    }
}

function delete_bug() {
    delete_it =  confirm("Delete: Sure? All content with this bug will be gone!");
    
    if(delete_it) {
	$.get("/delete_bug?id="+$.trim($("#bugid").text()), 
	      function(data) {
		  window.location.href = "../";
	      });
    }
}

function delete_wiki() {
    delete_it =  confirm("Delete: Sure? All content with this wiki will be gone!");
    
    if(delete_it) {
	$.get("/delete_wiki?id="+$.trim($("#pageid").text()), 
	      function(data) {
		  	window.location.href = "../";
	      });
    }
}

$(document).ready(function(){
    enable_hotkeys();
});

