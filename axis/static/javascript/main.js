console.log("This is Captain Kirk speaking.")

//////// functions to get project id and attach it to posts for updates
let projectId;
let allUpdateButtons = document.querySelectorAll(".openUpdateModal");
allUpdateButtons.forEach( (ele) => {
	ele.addEventListener('click', setProjectId);
});
//update route to use the correct project id
function setProjectId (event) {
    projectId = event.target.getAttribute('data-projectid');
    document.projectUpdateForm.action = `project/${projectId}/update`
}

/////// functions to get the correct project id and save it for updates that require project id 
// make a call to server get info and prepopolate form
