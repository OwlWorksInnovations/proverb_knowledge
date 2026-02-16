function pushToTalk() {
    let pushToTalkBtn = document.querySelector("#pushToTalkBtn")

    pushToTalkBtn.addEventListener("mousedown", () => {
        recordAudio()
    })

    pushToTalkBtn.addEventListener("mouseup", () => {
        stopAudio()
    })
}

function recordAudio() {
    eel.recordAudio();
}
function stopAudio() {
    eel.stopAudio()
}

eel.expose(updateQuestionText)
function updateQuestionText(question) {
    let questionText = document.querySelector("#question")
    questionText.innerHTML = question
}

eel.expose(updateAnswerText)
function updateAnswerText(answer) {
    let answerText = document.querySelector("#answer")
    answerText.innerHTML = answer
}
