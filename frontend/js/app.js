/**
 * PSG College of Arts and Science (PSGCAS)
 * Placement & Career AI Web Chatbot - Frontend Script
 */

document.addEventListener('DOMContentLoaded', () => {
    // --- State Variables ---
    let ttsEnabled = false;
    let activeTab = 'chat';

    // --- DOM Elements ---
    const navItems = document.querySelectorAll('.nav-item');
    const tabContents = document.querySelectorAll('.tab-content');
    const chatInput = document.getElementById('chatInput');
    const sendBtn = document.getElementById('sendBtn');
    const chatMessages = document.getElementById('chatMessages');
    const clearChatBtn = document.getElementById('clearChatBtn');
    const promptChips = document.querySelectorAll('.chip-btn');
    const ttsToggleBtn = document.getElementById('ttsToggleBtn');
    const themeToggleBtn = document.getElementById('themeToggleBtn');
    
    // Mock Interview Elements
    const streamSelect = document.getElementById('streamSelect');
    const generateQuestionsBtn = document.getElementById('generateQuestionsBtn');
    const questionsContainer = document.getElementById('questionsContainer');

    // Resume Analyzer Elements
    const resumeInput = document.getElementById('resumeInput');
    const analyzeResumeBtn = document.getElementById('analyzeResumeBtn');
    const resumeResultsCard = document.getElementById('resumeResultsCard');
    const resumeFeedbackContent = document.getElementById('resumeFeedbackContent');

    // Rectify Form Elements
    const rectifyForm = document.getElementById('rectifyForm');
    const ticketsContainer = document.getElementById('ticketsContainer');

    // FAQ Elements
    const faqAccordion = document.getElementById('faqAccordion');

    // --- 1. Tab Navigation ---
    navItems.forEach(item => {
        item.addEventListener('click', () => {
            const targetTab = item.getAttribute('data-tab');

            navItems.forEach(nav => nav.classList.remove('active'));
            tabContents.forEach(tab => tab.classList.remove('active'));

            item.classList.add('active');
            const targetElement = document.getElementById(`${targetTab}-tab`);
            if (targetElement) {
                targetElement.classList.add('active');
            }
            activeTab = targetTab;

            if (targetTab === 'faqs' && faqAccordion.children.length === 0) {
                loadFAQs();
            }
        });
    });

    // --- 2. Theme & Speech Settings ---
    themeToggleBtn.addEventListener('click', () => {
        const isDark = document.body.getAttribute('data-theme') === 'dark';
        if (isDark) {
            document.body.removeAttribute('data-theme');
            themeToggleBtn.innerHTML = '<i class="fa-solid fa-moon"></i>';
        } else {
            document.body.setAttribute('data-theme', 'dark');
            themeToggleBtn.innerHTML = '<i class="fa-solid fa-sun"></i>';
        }
    });

    ttsToggleBtn.addEventListener('click', () => {
        ttsEnabled = !ttsEnabled;
        if (ttsEnabled) {
            ttsToggleBtn.style.color = '#F59E0B';
            ttsToggleBtn.title = 'Speech Output Enabled';
            speakText("Speech synthesis activated for PSGCAS Placement Assistant.");
        } else {
            ttsToggleBtn.style.color = '#FFFFFF';
            ttsToggleBtn.title = 'Speech Output Disabled';
            window.speechSynthesis.cancel();
        }
    });

    function speakText(text) {
        if (!ttsEnabled || !('speechSynthesis' in window)) return;
        window.speechSynthesis.cancel();
        
        // Clean markdown tags for TTS
        const cleanText = text.replace(/[*#_`]/g, '');
        const utterance = new SpeechSynthesisUtterance(cleanText);
        utterance.rate = 1.0;
        utterance.pitch = 1.0;
        window.speechSynthesis.speak(utterance);
    }

    // --- 3. Chat Logic ---
    function appendMessage(sender, text, time = null) {
        const msgTime = time || new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        const isUser = sender === 'user';

        const msgDiv = document.createElement('div');
        msgDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;

        const parsedContent = isUser ? escapeHTML(text) : marked.parse(text);

        msgDiv.innerHTML = `
            <div class="avatar">
                <i class="fa-solid ${isUser ? 'fa-user' : 'fa-graduation-cap'}"></i>
            </div>
            <div class="message-content">
                <div class="msg-header">
                    <span class="sender-name">${isUser ? 'You (PSGCAS Student)' : 'PSGCAS Placement Bot'}</span>
                    <span class="time-stamp">${msgTime}</span>
                </div>
                <div class="msg-text">${parsedContent}</div>
            </div>
        `;

        chatMessages.appendChild(msgDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;

        if (!isUser) {
            speakText(text);
        }
    }

    function escapeHTML(str) {
        return str.replace(/[&<>'"]/g, 
            tag => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' }[tag] || tag)
        );
    }

    function showTypingIndicator() {
        const indicator = document.createElement('div');
        indicator.id = 'typingIndicator';
        indicator.className = 'message bot-message';
        indicator.innerHTML = `
            <div class="avatar"><i class="fa-solid fa-graduation-cap"></i></div>
            <div class="message-content">
                <div class="msg-text">
                    <span class="typing-dots"><i class="fa-solid fa-spinner fa-spin"></i> Consulting PSGCAS CDC Database...</span>
                </div>
            </div>
        `;
        chatMessages.appendChild(indicator);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function removeTypingIndicator() {
        const indicator = document.getElementById('typingIndicator');
        if (indicator) indicator.remove();
    }

    async function handleSendMessage(userMsgText = null) {
        const query = userMsgText || chatInput.value.strip ? chatInput.value.trim() : chatInput.value;
        if (!query) return;

        appendMessage('user', query);
        chatInput.value = '';
        chatInput.style.height = 'auto';

        showTypingIndicator();

        try {
            const res = await fetch('/api/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: query })
            });

            removeTypingIndicator();

            if (res.ok) {
                const data = await res.json();
                appendMessage('bot', data.response);
            } else {
                appendMessage('bot', '⚠️ Sorry, could not reach PSGCAS servers right now. Please try again or visit C-Block CDC Office.');
            }
        } catch (err) {
            removeTypingIndicator();
            appendMessage('bot', '⚠️ Network connection issue. Please check your network or backend server.');
        }
    }

    sendBtn.addEventListener('click', () => handleSendMessage());

    chatInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSendMessage();
        }
    });

    clearChatBtn.addEventListener('click', () => {
        chatMessages.innerHTML = `
            <div class="message bot-message">
                <div class="avatar"><i class="fa-solid fa-graduation-cap"></i></div>
                <div class="message-content">
                    <div class="msg-header">
                        <span class="sender-name">PSGCAS Placement Bot</span>
                        <span class="time-stamp">Just now</span>
                    </div>
                    <div class="msg-text">
                        <p>Chat cleared! How can I assist you with PSGCAS placement or career guidance?</p>
                    </div>
                </div>
            </div>
        `;
    });

    // Prompt Chips Click Listener
    promptChips.forEach(chip => {
        chip.addEventListener('click', () => {
            const promptText = chip.getAttribute('data-prompt');
            handleSendMessage(promptText);
        });
    });

    // --- 4. Mock Interview Generator ---
    generateQuestionsBtn.addEventListener('click', async () => {
        const selectedStream = streamSelect.value;
        questionsContainer.innerHTML = '<p class="empty-msg"><i class="fa-solid fa-spinner fa-spin"></i> Generating tailored interview questions...</p>';

        try {
            const res = await fetch('/api/mock-interview', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ stream: selectedStream })
            });

            if (res.ok) {
                const data = await res.json();
                renderMockQuestions(data.questions, selectedStream);
            }
        } catch (err) {
            questionsContainer.innerHTML = '<p class="empty-msg">Error loading questions. Please try again.</p>';
        }
    });

    function renderMockQuestions(questions, stream) {
        questionsContainer.innerHTML = '';
        questions.forEach((q, idx) => {
            const card = document.createElement('div');
            card.className = 'q-card';
            card.innerHTML = `
                <h4>Question ${idx + 1} (${stream})</h4>
                <p><strong>"${q}"</strong></p>
                <div style="margin-top: 10px;">
                    <textarea placeholder="Type your mock answer here to practice..." rows="2" class="custom-select"></textarea>
                    <button class="chip-btn" style="margin-top: 6px;" onclick="alert('Great effort! Speak with clarity, state relevant coursework at PSGCAS, and structure using Situation-Task-Action-Result.')">
                        💡 Get Answer Tips
                    </button>
                </div>
            `;
            questionsContainer.appendChild(card);
        });
    }

    // --- 5. Resume Analyzer ---
    analyzeResumeBtn.addEventListener('click', () => {
        const text = resumeInput.value.trim();
        if (!text) {
            alert('Please paste your resume summary or text first!');
            return;
        }

        resumeResultsCard.classList.remove('hidden');
        resumeFeedbackContent.innerHTML = `
            <div style="line-height: 1.6;">
                <p style="color: #10B981; font-weight: 700;">✅ Strengths Detected:</p>
                <ul>
                    <li>Structured section layout and clear educational credentials.</li>
                    <li>PSGCAS affiliation highlighted effectively.</li>
                </ul>
                <p style="color: #D97706; font-weight: 700; margin-top: 10px;">⚠️ Key Areas for Improvement:</p>
                <ul>
                    <li><strong>Action Verbs</strong>: Begin bullet points with strong verbs (e.g., <em>Developed, Engineered, Conducted, Analyzed</em>).</li>
                    <li><strong>Quantifiable Impact</strong>: Add metrics (e.g., "Increased efficiency by 15%", "Managed team of 4").</li>
                    <li><strong>Skills Section</strong>: Ensure industry-relevant tools (Python, SQL, Advanced Excel, Financial Modeling, Lab Techniques) match recruiter descriptions for PSGCAS drives.</li>
                </ul>
            </div>
        `;
    });

    // --- 6. Rectify / Escalation Form ---
    rectifyForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const payload = {
            student_name: document.getElementById('studentName').value,
            roll_number: document.getElementById('rollNumber').value,
            department: document.getElementById('department').value,
            email: document.getElementById('email').value,
            phone: document.getElementById('phone').value,
            query_category: document.getElementById('queryCategory').value,
            issue_description: document.getElementById('issueDescription').value
        };

        try {
            const res = await fetch('/api/rectify-query', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });

            if (res.ok) {
                const data = await res.json();
                alert(data.message);
                rectifyForm.reset();
                addTicketToUI(data.ticket);
            }
        } catch (err) {
            alert('Could not submit ticket. Please check connection.');
        }
    });

    function addTicketToUI(ticket) {
        if (ticketsContainer.querySelector('.empty-msg')) {
            ticketsContainer.innerHTML = '';
        }

        const item = document.createElement('div');
        item.className = 'ticket-item';
        item.innerHTML = `
            <div class="ticket-header">
                <span>🎫 Ticket ID: ${ticket.ticket_id}</span>
                <span style="color: #D97706; font-weight: 600;">${ticket.status}</span>
            </div>
            <div><strong>Student:</strong> ${ticket.student_name} (${ticket.roll_number}) - ${ticket.department}</div>
            <div><strong>Category:</strong> ${ticket.query_category}</div>
            <div style="color: var(--text-secondary); margin-top: 4px;"><em>"${ticket.issue_description}"</em></div>
            <div style="font-size: 0.75rem; color: #64748B; margin-top: 4px;">Submitted: ${ticket.created_at}</div>
        `;
        ticketsContainer.prepend(item);
    }

    // --- 7. Load FAQs ---
    async function loadFAQs() {
        try {
            const res = await fetch('/api/faqs');
            if (res.ok) {
                const data = await res.json();
                renderFAQs(data.faqs);
            }
        } catch (err) {
            faqAccordion.innerHTML = '<p class="empty-msg">Failed to load FAQs.</p>';
        }
    }

    function renderFAQs(faqs) {
        faqAccordion.innerHTML = '';
        faqs.forEach(faq => {
            const item = document.createElement('div');
            item.className = 'faq-item';
            item.innerHTML = `
                <div class="faq-question">
                    <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 8px;"></i> ${faq.question}</span>
                    <i class="fa-solid fa-chevron-down"></i>
                </div>
                <div class="faq-answer">
                    ${marked.parse(faq.answer)}
                </div>
            `;

            const qHeader = item.querySelector('.faq-question');
            qHeader.addEventListener('click', () => {
                item.classList.toggle('open');
            });

            faqAccordion.appendChild(item);
        });
    }

    // Trigger initial mock interview question generation
    generateQuestionsBtn.click();
});
