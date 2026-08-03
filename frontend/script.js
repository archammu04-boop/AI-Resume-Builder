const API_BASE_URL = "http://13.232.140.179:8000";
document.getElementById("generateBtn").addEventListener("click", async () => {

    const data = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        phone: document.getElementById("phone").value,
        education: document.getElementById("education").value,
        skills: document.getElementById("skills").value,
        projects: document.getElementById("projects").value,
        experience: document.getElementById("experience").value
    };

    try {

        document.getElementById("resume-output").innerHTML =
            "<p>Generating Resume...</p>";

        document.getElementById("ats-output").innerHTML =
            "<p>Analyzing ATS Score...</p>";

        // Generate Resume
        const resumeResponse = await fetch(`${API_BASE_URL}/generate`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(data)

        });

        const resumeResult = await resumeResponse.json();

        document.getElementById("resume-output").innerHTML =
            marked.parse(resumeResult.resume);

        // Generate ATS Score
        
        const atsResponse=await fetch(`${API_BASE_URL}/ats`, {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(data)

        });

        const atsResult = await atsResponse.json();

        document.getElementById("ats-output").innerHTML =
            marked.parse(atsResult.ats);

    }

    catch (error) {

        console.error(error);

        document.getElementById("resume-output").innerHTML =
            "<p style='color:red;'>Failed to generate resume.</p>";

        document.getElementById("ats-output").innerHTML =
            "<p style='color:red;'>Failed to analyze ATS score.</p>";

    }

});

document.getElementById("downloadBtn").addEventListener("click", () => {

    const element = document.getElementById("resume-output");

    const options = {

        margin: 0.5,

        filename: "Resume.pdf",

        image: {
            type: "jpeg",
            quality: 1
        },

        html2canvas: {
            scale: 2,
            useCORS: true,
            scrollY: 0
        },

        jsPDF: {
            unit: "in",
            format: "a4",
            orientation: "portrait"
        },

        pagebreak: {
            mode: ["avoid-all", "css", "legacy"]
        }

    };

    html2pdf()
        .set(options)
        .from(element)
        .save();

});


document.getElementById("improveBtn").addEventListener("click", async () => {

    try {

        const resume = document.getElementById("resume-output").innerText;

        document.getElementById("improved-output").innerHTML =
            "<p>Improving Resume...</p>";

        const response=await fetch(`${API_BASE_URL}/improve`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                resume: resume
            })

        });

        const result = await response.json();

        document.getElementById("improved-output").innerHTML =
            marked.parse(result.resume);

    }
    catch (error) {

        console.error(error);

        document.getElementById("improved-output").innerHTML =
            "<p style='color:red;'>Failed to improve resume.</p>";

    }

});

document.getElementById("coverBtn").addEventListener("click", async () => {

    const data = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        phone: document.getElementById("phone").value,
        education: document.getElementById("education").value,
        skills: document.getElementById("skills").value,
        projects: document.getElementById("projects").value,
        experience: document.getElementById("experience").value
    };

    try {

        document.getElementById("cover-output").innerHTML =
            "<p>Generating Cover Letter...</p>";

        const response=await fetch(`${API_BASE_URL}/cover-letter`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(data)

        });

        const result = await response.json();

        document.getElementById("cover-output").innerHTML =
            marked.parse(result.cover);

    }

    catch(error){

        console.error(error);

        document.getElementById("cover-output").innerHTML =
            "<p style='color:red;'>Failed to generate Cover Letter.</p>";

    }

});

document.getElementById("linkedinBtn").addEventListener("click", async () => {

    const data = {
        name: document.getElementById("name").value,
        education: document.getElementById("education").value,
        skills: document.getElementById("skills").value,
        projects: document.getElementById("projects").value,
        experience: document.getElementById("experience").value
    };

    try {

        document.getElementById("linkedin-output").innerHTML =
            "<p>Generating LinkedIn Summary...</p>";

        const response=await fetch(`${API_BASE_URL}/linkedin`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(data)

        });

        const result = await response.json();

        document.getElementById("linkedin-output").innerHTML =
            marked.parse(result.linkedin);

    }

    catch(error){

        console.error(error);

        document.getElementById("linkedin-output").innerHTML =
            "<p style='color:red;'>Failed to generate LinkedIn Summary.</p>";

    }

});