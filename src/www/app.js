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
    let answerText = document.querySelector("#answer");
    const symbol = "&";

    const startPos = answer.indexOf(symbol) + 1;
    const endPos = answer.lastIndexOf(symbol);
    const result = answer.substring(startPos, endPos);

    const cleanAnswer = answer.replaceAll(`&${result}&`, "");
    answerText.innerHTML = cleanAnswer;

    const explainDiv = document.createElement("div");
    explainDiv.innerHTML = result;
    explainDiv.classList.add("card-subtitle");
    explainDiv.style.color = "#bbbbbb";
    explainDiv.style.fontStyle = "italic";
    explainDiv.style.fontSize = "small";

    answerText.appendChild(explainDiv);
}