        // List of solution files and challenge names
        const solutions = [
            { day: 1, file: 'Day_01/wordle.py', name: 'Wordle 🟩' },
            { day: 2, file: 'Day_02/bloodmoon.py', name: 'Blood Moon 🩸' },
            { day: 3, file: 'Day_03/holi.py', name: 'Holi 🌈' },
            { day: 4, file: 'Day_04/homebrew_computer_club.py', name: 'Homebrew Computer Club 🤓' },
            { day: 5, file: 'Day_05/alysa_liu.py', name: 'Alysa Liu ⛸️' },
            { day: 6, file: 'Day_06/daylight_savings.py', name: 'Daylight Savings ⏰' },
            { day: 7, file: 'Day_07/womens_day.py', name: 'International Women’s Day 💖' },
            { day: 8, file: 'Day_08/sputnik9.py', name: 'Sputnik 9 🚀' },
            { day: 9, file: 'Day_09/ringring.py', name: 'Ring Ring ☎️' },
            { day: 10, file: 'Day_10/hitchhikers_guide.py', name: "Hitchhiker's Guide 🪐" },
            { day: 11, file: 'Day_11/www.py', name: 'World Wide Web 🌐' },
            { day: 12, file: 'Day_12/palindrome.py', name: 'Palindrome 🏎️' },
            { day: 13, file: 'Day_13/pi_day.py', name: 'Pi Day 🥧' },
            { day: 14, file: 'Day_14/caesar_cipher.py', name: 'Caesar Cipher 🏛️' },
            { day: 15, file: 'Day_15/oscars.py', name: 'Oscars 2026 🏆' },
            { day: 16, file: 'Day_16/green_chicago_river.py', name: 'Green Chicago River ☘️' },
            { day: 17, file: 'Day_17/flight_vouchers.py', name: 'Flight Vouchers 🏖️' },
            { day: 18, file: 'Day_16/', name: '❓❓❓' },
            { day: 19, file: 'Day_16/', name: '❓❓❓' },
            { day: 20, file: 'Day_16/', name: '❓❓❓' },
            { day: 21, file: 'Day_16/', name: '❓❓❓' },
            { day: 22, file: 'Day_16/', name: '❓❓❓' },
            { day: 23, file: 'Day_16/', name: '❓❓❓' },
            { day: 24, file: 'Day_16/', name: '❓❓❓' },
            { day: 25, file: 'Day_16/', name: '❓❓❓' },
            { day: 26, file: 'Day_16/', name: '❓❓❓' },
            { day: 27, file: 'Day_16/', name: '❓❓❓' },
            { day: 28, file: 'Day_16/', name: '❓❓❓' },
            { day: 29, file: 'Day_16/', name: '❓❓❓' },
            { day: 30, file: 'Day_16/', name: '❓❓❓' }
        ];

        let challengeLinks = {};

        // Load challenge links
        fetch('Assets/challenges.json')
            .then(response => response.json())
            .then(data => {
                challengeLinks = data;
            })
            .catch(error => console.error('Error loading challenge links:', error));
        const list = document.getElementById('solution-list');
        const codeViewer = document.getElementById('code-viewer');
        const modalBackdrop = document.getElementById('modal-backdrop');

        function closeModal() {
            codeViewer.classList.remove('active');
            modalBackdrop.classList.remove('active');
            document.body.classList.remove('modal-open');
        }

        solutions.forEach(sol => {
            const li = document.createElement('li');
            li.innerHTML = `<div class="day-box">Day ${String(sol.day).padStart(2, '0')}</div><div class="challenge-box">${sol.name}</div>`;
            li.onclick = async () => {
                codeViewer.classList.add('active');
                modalBackdrop.classList.add('active');
                document.body.classList.add('modal-open');
                
                codeViewer.innerHTML = 
                `<div class="modal-header">
                    <h2 class="modal-title">Day ${sol.day}: ${sol.name}</h2>
                    <button class="modal-close-btn">✕</button></div>
                    <div class="modal-content"><span style="color: #3498db;">Loading content...</span>
                </div>`;

                try {
                    const dayStr = String(sol.day).padStart(2, '0');

                    const imgSrc = `Day_${dayStr}/${dayStr}.png`;

                    const expFile = `Day_${dayStr}/explanation.txt`;

                    const codeResp = await fetch(sol.file);
                    if (!codeResp.ok) throw new Error('Code file not found');
                    const code = await codeResp.text();

                    const expResp = await fetch(expFile);

                    if (!expResp.ok) throw new Error('Explanation file not found');

                    const explanation = await expResp.text();
                    const escapedCode = code.replace(/[<>]/g, c => ({'<':'&lt;','>':'&gt;'}[c]));

                    const escapedExp = explanation.replace(/\n/g, '<br>');
                    
                    let challengeButton = '';
                    const dayKey = String(sol.day).padStart(2, '0');
                    if (challengeLinks[dayKey]) {
                        challengeButton = `<div style="text-align: center; margin-top: 20px;">
                            <a href="${challengeLinks[dayKey]}" target="_blank" style="text-decoration: none;">
                                <button class="challenge-btn">Try Challenge</button>
                            </a>
                        </div>`;
                    }
                    
                    codeViewer.innerHTML = `<div class="modal-header">
                        <h2 class="modal-title">Day ${sol.day}: ${sol.name}</h2>
                        <button class="modal-close-btn">✕</button></div>
                        <div class="modal-content"><img class="modal-image" src="${imgSrc}" alt="Day ${sol.day}">
                        <div class="subheading">My Solution</div>
                         <pre><code class="language-python">${escapedCode}</code></pre>
                        <div class="subheading">Explanation</div>
                        <div class="explanation">${escapedExp}</div>${challengeButton}</div>`;
                    Prism.highlightAll();
                } catch (e) {
                    codeViewer.innerHTML = `<div class="modal-header"><h2 class="modal-title">Day ${sol.day}: ${sol.name}</h2><button class="modal-close-btn">✕</button></div><div class="modal-content"><span style="color:#3498db; font-size: 1.2rem; text-align: center; display: block;">Coming Soon!</span></div>`;
                }
            };
            list.appendChild(li);
        });

        // Use event delegation for the close button
        codeViewer.addEventListener('click', (e) => {
            if (e.target.classList.contains('modal-close-btn')) {
                closeModal();
            }
        });

        // Close modal when clicking backdrop
        modalBackdrop.onclick = closeModal;

        // Close modal on Escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && codeViewer.classList.contains('active')) {
                closeModal();
            }
        });

        function scrollToChallenges() {
            document.getElementById('solution-list').scrollIntoView({ behavior: 'smooth' });
        }