
function notLoggedIn(){
    alert('not logged in');
}

// reference https://testdriven.io/blog/django-ajax-xhr/
function upVote(id){
    fetch(`${window.location.origin}/insQuire/categories/question/upvote/`, { 
        method: 'POST',
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify({ question_id:id })  // Send the question id in the request body
    }
    )
    .then(response => response.json())
    .then(data => {
        console.log(data)
        // Update the vote count in the HTML
        var votes = document.getElementById('votes' + id);
        votes.textContent = 'votes: ' + data.votes;
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
        body: JSON.stringify({ question_id:id })  // Send the question id in the request body
    }
    )
    .then(response => response.json())
    .then(data => {
        console.log(data)
        var votes = document.getElementById('votes' + id);
        votes.textContent = 'votes: ' + data.votes;
    }
    )
}


// https://docs.djangoproject.com/en/3.0/ref/csrf/#ajax
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}