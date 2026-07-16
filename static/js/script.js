document.addEventListener("DOMContentLoaded", () => {

    // ==========================
    // Elements
    // ==========================

    const form = document.getElementById("upload-form");

    const loader = document.getElementById("loader");

    const status = document.getElementById("status");

    const results = document.getElementById("results");

    const transcriptBox =
        document.getElementById("transcript-out");

    const summaryBox =
        document.getElementById("summary-out");

    const transcriptDownload =
        document.getElementById("download-transcript");

    const summaryDownload =
        document.getElementById("download-summary");


    // ==========================
    // Upload Form
    // ==========================

    form.addEventListener("submit", async (e) => {

        e.preventDefault();

        const file =
            document.getElementById("audio-file").files[0];

        if (!file) {

            alert("Please select an audio file.");

            return;
        }

        const formData = new FormData();

        formData.append("audio", file);


        loader.classList.remove("hidden");

        results.classList.add("hidden");

        status.innerHTML = "Uploading audio...";


        try {

            const response = await fetch("/upload", {

                method: "POST",

                body: formData

            });

            const data = await response.json();

            loader.classList.add("hidden");

            if (data.error) {

                status.innerHTML = data.error;

                return;

            }

            status.innerHTML = "Completed Successfully.";

            results.classList.remove("hidden");


            // ======================
            // Display Result
            // ======================

            transcriptBox.value =
                data.transcript;

            summaryBox.value =
                data.summary;


            // ======================
            // Download Transcript
            // ======================

            transcriptDownload.onclick = () => {

                downloadText(

                    data.transcript,

                    "transcript.txt"

                );

            };


            // ======================
            // Download Summary
            // ======================

            summaryDownload.onclick = () => {

                downloadText(

                    data.summary,

                    "summary.txt"

                );

            };

        }

        catch (error) {

            loader.classList.add("hidden");

            status.innerHTML =

                "Something went wrong.";

            console.log(error);

        }

    });


    // ==========================
    // Download Helper
    // ==========================

    function downloadText(text, filename) {

        const blob = new Blob(

            [text],

            {

                type: "text/plain"

            }

        );

        const url = URL.createObjectURL(blob);

        const a = document.createElement("a");

        a.href = url;

        a.download = filename;

        document.body.appendChild(a);

        a.click();

        document.body.removeChild(a);

        URL.revokeObjectURL(url);

    }

});