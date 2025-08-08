// script.js

// Bu kod, tüm HTML sayfası yüklendiğinde çalışmaya başlar.
document.addEventListener('DOMContentLoaded', () => {
    
    // Değişkenlerimizi HTML'den alıyoruz
    const cardContainer = document.getElementById('card-container');
    const searchInput = document.getElementById('search-input');
    const courseFilter = document.getElementById('course-filter');
    const examTypeFilter = document.getElementById('exam-type-filter');

    let allExamData = []; // Tüm veriyi saklayacağımız global değişken

    // Adım 1: Python'un oluşturduğu JSON verisini çekme
    async function loadData() {
        try {
            const response = await fetch('./data.json'); // Aynı klasördeki data.json'ı çek
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            allExamData = await response.json();
            
            // Veri yüklendikten sonra uygulamayı başlat
            initializeApp();

        } catch (error) {
            console.error("Veri yüklenirken bir hata oluştu:", error);
            cardContainer.innerHTML = '<p style="color: red; grid-column: 1 / -1; text-align: center;">Veri yüklenemedi. Lütfen data.json dosyasının mevcut olduğundan emin olun.</p>';
        }
    }

    // Adım 2: Uygulamayı başlatan ana fonksiyon
    function initializeApp() {
        populateFilters();
        addEventListeners();
        filterAndDisplay(); // Başlangıçta tüm kartları göster
    }

    // Adım 3: Filtreleri dinamik olarak doldurma
    function populateFilters() {
        const allCourses = [...new Set(allExamData.map(item => item.Course_Name))].sort();
        const allExamTypes = [...new Set(allExamData.map(item => item.Exam_Type))].sort();

        allCourses.forEach(course => {
            courseFilter.innerHTML += `<option value="${course}">${course}</option>`;
        });
        allExamTypes.forEach(type => {
            examTypeFilter.innerHTML += `<option value="${type}">${type}</option>`;
        });
    }
    
    // Adım 4: Olay dinleyicilerini ekleme
    function addEventListeners() {
        searchInput.addEventListener('input', filterAndDisplay);
        courseFilter.addEventListener('change', filterAndDisplay);
        examTypeFilter.addEventListener('change', filterAndDisplay);
    }

    // Adım 5: Kartları oluşturma ve filtreleme
    function filterAndDisplay() {
        const searchTerm = searchInput.value.toLowerCase();
        const selectedCourse = courseFilter.value;
        const selectedExamType = examTypeFilter.value;

        const filteredData = allExamData.filter(record => {
            const nameMatch = record.Student_Name.toLowerCase().includes(searchTerm);
            const courseMatch = selectedCourse === 'all' || record.Course_Name === selectedCourse;
            const examTypeMatch = selectedExamType === 'all' || record.Exam_Type === selectedExamType;
            return nameMatch && courseMatch && examTypeMatch;
        });
        
        displayCards(filteredData);
    }
    
    // Adım 6: Verilen dataya göre kartları ekrana çizme
    function displayCards(data) {
        cardContainer.innerHTML = '';
        if (data.length === 0) {
            cardContainer.innerHTML = '<p style="color: #aaa; grid-column: 1 / -1; text-align: center;">Filtrelere uygun sonuç bulunamadı.</p>';
            return;
        }
        data.forEach(record => {
            const card = document.createElement('div');
            card.className = 'card';
            const attendanceClass = record.Attendance_Status === 'present' ? 'present' : 'absent';
            const attendanceText = record.Attendance_Status === 'present' ? 'Katıldı' : 'Katılmadı';
            const scoreColor = record.Score >= 90 ? '#4CAF50' : record.Score >= 70 ? '#3498db' : record.Score >= 50 ? '#f1c40f' : '#c62828';

            card.innerHTML = `
                <div class="score-display" style="background-color: ${scoreColor};">
                    <div class="score-value">${record.Score}</div>
                    <div class="score-label">PUAN</div>
                </div>
                <div class="card-content">
                    <h3>${record.Student_Name}</h3>
                    <div class="card-info">
                        <div class="info-item">Ders: <span>${record.Course_Name}</span></div>
                        <div class="info-item">Sınav: <span>${record.Exam_Type}</span></div>
                        <div class="info-item">Devam: <span class="attendance-tag ${attendanceClass}">${attendanceText}</span></div>
                    </div>
                </div>
            `;
            cardContainer.appendChild(card);
        });
    }

    // Her şeyin başlangıç noktası: Veriyi yükle
    loadData();
});