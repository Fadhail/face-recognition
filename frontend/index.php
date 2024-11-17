<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Attendance System</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@1.9.6/dist/tailwind.min.css" rel="stylesheet">
    <style>
        /* Add any additional styles here */
    </style>
</head>
<body class="bg-gray-100 flex flex-col items-center justify-center h-screen">

    <h1 class="text-3xl font-bold mb-4">Attendance System</h1>
    <div class="flex justify-center mb-4">
        <img id="video" class="border border-gray-500" src="" alt="Video Feed" />
    </div>

    <div class="flex justify-center">
        <button id="captureButton" class="bg-blue-500 text-white px-4 py-2 rounded">Capture Attendance</button>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const videoElement = document.getElementById('video');
            videoElement.src = 'http://localhost:5000/video_feed'; // Update this if needed

            const captureButton = document.getElementById('captureButton');
            captureButton.addEventListener('click', function() {
                // Fetch data to send, here just a sample data
                const attendanceData = {
                    student_id: "12345",
                    name: "John Doe",
                    captured_at: new Date().toISOString()
                };

                fetch('http://localhost:5000/capture_attendance', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(attendanceData),
                })
                .then(response => response.json())
                .then(data => {
                    alert(data.message); // Show confirmation message
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
            });
        });
    </script>

</body>
</html>
