async function loadDashboard() {

    const response =
        await fetch(
            "http://127.0.0.1:5000/dashboard/1"
        );

    const data =
        await response.json();

    console.log(data);

    const chart =
        document.getElementById(
            "emotionChart"
        );

    const emotions =
        data.emotion_stats;

    const max =
        Math.max(
            ...emotions.map(
                e => e.total
            )
        );

    emotions.forEach(emotion => {

        const width =
            (emotion.total / max) * 100;

        chart.innerHTML += `
            <div class="emotion-row">

                <div class="emotion-header">

                    <span>
                        ${emotion.emotion}
                    </span>

                    <span>
                        ${emotion.total}
                    </span>

                </div>

                <div class="bar">

                    <div
                        class="fill"
                        style="width:${width}%"
                    ></div>

                </div>

            </div>
        `;
    });
}

loadDashboard();