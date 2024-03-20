// alerts user when they are not logged in
function notLoggedIn(){
    alert('not logged in');
}

// reference from https://testdriven.io/blog/django-ajax-xhr/
function upVote(id){
    fetch(`${window.location.origin}/insQuire/categories/question/upvote/`, { 
        method: 'POST',
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify({ question_id:id })  // Send question id in request body
        }
    )
    .then(response => response.json()) // response from fetch is converted to json
    .then(voteReturn => { // json format file, from response.json() promise
        console.log(voteReturn)
        // Update the vote count in the HTML
        var votes = document.getElementById('votes' + id);
        votes.textContent = voteReturn.votes; // the updated votes are retrived from json file and set
        }
    )
}

function downVote(id){
    fetch(`${window.location.origin}/insQuire/categories/question/downvote/`, { 
        method: 'POST',
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify({ question_id:id })  
    }
    )
    .then(response => response.json()) 
    .then(voteReturn => { 
        console.log(voteReturn)
        var votes = document.getElementById('votes' + id);
        votes.textContent = voteReturn.votes; 
    }
    )
}


// reference from https://docs.djangoproject.com/en/3.0/ref/csrf/#ajax
function getCookie(name) {
    var cookieVal = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieVal = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieVal;
}
