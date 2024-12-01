document.addEventListener("DOMContentLoaded", () => {
    console.log("JavaScript Loaded!");

    // Handle video upload
    const uploadForm = document.getElementById("uploadForm");
    if (uploadForm) {
        uploadForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const formData = new FormData(uploadForm);
            const response = await fetch("/videos/upload", {
                method: "POST",
                body: formData,
            });
            const result = await response.json();
            const uploadStatus = document.getElementById("uploadStatus");
            if (response.ok) {
                uploadStatus.innerText = "Video uploaded successfully!";
                uploadStatus.style.color = "green";
            } else {
                uploadStatus.innerText = `Error: ${result.message}`;
                uploadStatus.style.color = "red";
            }
        });
    }

    // Handle video search
    const searchForm = document.getElementById("searchForm");
    if (searchForm) {
        searchForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const query = document.getElementById("query").value;
            const response = await fetch(`/search?q=${encodeURIComponent(query)}`);
            const results = await response.json();
            const resultsList = document.getElementById("searchResults");
            resultsList.innerHTML = results
                .map((video) => `<li><a href="/stream.html?video_id=${video.id}">${video.title}</a></li>`)
                .join("");
        });
    }

    // Handle video streaming
    const videoPlayer = document.getElementById("videoPlayer");
    const videoTitle = document.getElementById("videoTitle");
    const videoDescription = document.getElementById("videoDescription");
    const resolutionSelector = document.getElementById("resolutionSelector");

    async function fetchVideoMetadata(videoId) {
        const response = await fetch(`/videos/stream/${videoId}`);
        if (response.ok) {
            const videoData = await response.json();
            videoTitle.innerText = videoData.title;
            videoDescription.innerText = videoData.description;
            const s3Urls = videoData.s3_urls;

            for (const [resolution, url] of Object.entries(s3Urls)) {
                const option = document.createElement("option");
                option.value = url;
                option.innerText = resolution;
                resolutionSelector.appendChild(option);
            }
        } else {
            videoTitle.innerText = "Video not found!";
        }
    }

    if (resolutionSelector) {
        const urlParams = new URLSearchParams(window.location.search);
        const videoId = urlParams.get("video_id");
        if (videoId) {
            fetchVideoMetadata(videoId);
        }

        resolutionSelector.addEventListener("change", () => {
            const selectedUrl = resolutionSelector.value;
            if (selectedUrl) {
                videoPlayer.src = selectedUrl;
                videoPlayer.load();
                videoPlayer.play();
            }
        });
    }
});
