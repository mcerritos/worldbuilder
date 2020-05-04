console.log("This is Captain Kirk speaking.")

// attach event listener to all update buttons
let projectId;
let allUpdateButtons = document.querySelectorAll(".openUpdateModal");
allUpdateButtons.forEach( (ele) => {
	ele.addEventListener('click', setProjectId);
});
//update route to use the correct project is
function setProjectId (event) {
    projectId = event.target.getAttribute('data-projectid');
    document.projectUpdateForm.action = `project/${projectId}/update`
}

