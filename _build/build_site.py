"""Build the Flexible Visual Programming landing (ID default, EN) + 12-meetings pages.

Usage: python3 -I build_site.py <repo_dir>
Outputs: index.html (id), en/index.html, meetings/index.html (id), en/meetings/index.html
"""
import os
import sys

REPO = sys.argv[1]
BASE = "https://pavelkokora-oss.github.io/flexible-vp-landing/"
WA_NUM = "622130949485"
WA_TEXT = {
    "en": "I%E2%80%99m%20interested.%20I%20want%20to%20buy%20Flexible%20format.",
    "id": "Saya%20tertarik.%20Saya%20ingin%20membeli%20format%20Fleksibel.",
}
CURRICULUM = "https://test.algonova.id/sales/new/curriculum/visual-coding?fb_pixel_id=1152940395642591"

# ------------------------------------------------------------------ strings
T = {
    "title": ("Visual Programming — Flexible Format | Algonova", "Pemrograman Visual — Format Fleksibel | Algonova"),
    "desc": ("The same Visual Programming course in a flexible format: short lessons with a video, a quiz and a simulator, daily chat support, a live meeting every 3 weeks. 3× cheaper.",
             "Kursus Pemrograman Visual yang sama dalam format fleksibel: pelajaran singkat dengan video, kuis, dan simulator, bantuan chat setiap hari, pertemuan live setiap 3 minggu. 3× lebih murah."),
    "ogdesc": ("The same coding course. 3× cheaper.", "Kursus coding yang sama. 3× lebih murah."),
    "navtag": ("Visual Programming · Ages 8–11", "Pemrograman Visual · Usia 8–11 tahun"),
    "langlabel": ("Language", "Bahasa"),
    # hero
    "h_eyebrow": ("Visual Programming · New flexible format", "Pemrograman Visual · Format fleksibel baru"),
    "h1a": ("The same coding course.", "Kursus coding yang sama."),
    "h1b": ("3× cheaper.", "3× lebih murah."),
    "h_lead": ("Your child learns at home with <strong>weekly short lessons</strong> (video, quiz, simulator and tasks). Every 3 weeks, a <strong>live meeting</strong> with a tutor in a group of 4 kids. Same 36 topics, same certificate.",
               "Anak belajar di rumah dengan <strong>pelajaran singkat setiap minggu</strong> (video, kuis, simulator, dan tugas). Setiap 3 minggu ada <strong>pertemuan live</strong> bersama tutor dalam grup berisi 4 anak. 36 topik yang sama, sertifikat yang sama."),
    "cta_buy": ("I want to buy", "Saya ingin membeli"),
    "cta_more": ("See what's included", "Lihat apa saja yang didapat"),
    "chip1": ("Short video lessons", "Video pelajaran singkat"),
    "chip2": ("Simulators", "Simulator"),
    "chip3": ("Live meetings in groups of 4", "Pertemuan live dalam grup 4 anak"),
    "chip4": ("Chat support every day", "Bantuan chat setiap hari"),
    "stat_label": ("Flexible format vs regular format", "Format fleksibel vs format reguler"),
    "stat_word": ("cheaper", "lebih murah"),
    "stat_sub": ("per lesson — same topics and certificate", "per pelajaran — topik dan sertifikat yang sama"),
    # included
    "inc_eyebrow": ("What's included", "Yang didapat"),
    "inc_h2": ("Everything your child needs to learn coding", "Semua yang dibutuhkan anak untuk belajar coding"),
    "inc_total": ("36 lessons + 12 live meetings over 36 weeks", "36 pelajaran + 12 pertemuan live selama 36 minggu"),
    "c1t": ("36 lessons, one a week", "36 pelajaran, satu per minggu"),
    "c1d": ("Each lesson is 3–5 short parts of 15–20 minutes: a video, a quiz, a simulator and Scratch tasks.",
            "Setiap pelajaran terdiri dari 3–5 bagian singkat, masing-masing 15–20 menit: video, kuis, simulator, dan tugas Scratch."),
    "c2t": ("12 live meetings with a tutor", "12 pertemuan live bersama tutor"),
    "c2d": ("90 minutes in a premium mini-group of 4 students, every 3 weeks.", "90 menit dalam grup kecil premium berisi 4 siswa, setiap 3 minggu."),
    "c3t": ("Simulators", "Simulator"),
    "c3d": ("Interactive puzzles where your child tries an idea before coding it. The regular course doesn't have them.",
            "Teka-teki interaktif tempat anak mencoba ide sebelum menuliskannya dalam kode. Kursus reguler tidak memilikinya."),
    "c4t": ("Chat support every day", "Bantuan chat setiap hari"),
    "c4d": ("In Discord, 12:00–20:00 WIB. A moderator answers first, tutors help with harder questions.",
            "Di Discord, pukul 12:00–20:00 WIB. Moderator menjawab lebih dulu, tutor membantu pertanyaan yang lebih sulit."),
    "c5t": ("Reports for parents", "Laporan untuk orang tua"),
    "c5d": ("A short WhatsApp message every week and a PDF report after every 3 weeks.",
            "Pesan WhatsApp singkat setiap minggu dan laporan PDF setiap 3 minggu."),
    "c6t": ("Certificate", "Sertifikat"),
    "c6d": ("The same 36 topics as the regular course. A certificate is issued at the end.",
            "36 topik yang sama dengan kursus reguler. Sertifikat diberikan di akhir kursus."),
    "new": ("New", "Baru"),
    "all12": ("See all 12 meetings", "Lihat semua 12 pertemuan"),
    # lesson
    "l_eyebrow": ("Inside a lesson", "Isi satu pelajaran"),
    "l_h2": ("A lesson is more than one video", "Satu pelajaran lebih dari sekadar satu video"),
    "l_lead": ("One lesson a week: 3–5 short parts of 15–20 min with a video, a quiz, a simulator and Scratch tasks. Questions go to the tutor and the community team in Discord.",
               "Satu pelajaran per minggu: 3–5 bagian singkat 15–20 menit berisi video, kuis, simulator, dan tugas Scratch. Pertanyaan diajukan ke tutor dan tim komunitas di Discord."),
    "p1t": ("Video", "Video"), "p1d": ("The teacher explains the topic.", "Guru menjelaskan topik."),
    "p2t": ("Quiz", "Kuis"), "p2d": ("A quick check that the idea is clear.", "Cek singkat apakah materi sudah dipahami."),
    "p3t": ("Simulator", "Simulator"), "p3d": ("Try the idea in an interactive puzzle.", "Coba idenya dalam teka-teki interaktif."),
    "p4t": ("Scratch tasks", "Tugas Scratch"), "p4d": ("Build it with real code blocks.", "Wujudkan dengan blok kode sungguhan."),
    "cap_lesson": ("A piece of a real lesson: Kevin explains the topic · 55 sec", "Cuplikan pelajaran asli: Kevin menjelaskan topik · 55 detik"),
    "cap_map": ("The course map on the learning platform", "Peta kursus di platform belajar"),
    "sim_h3": ("Simulators: our main new feature", "Simulator: fitur baru utama kami"),
    "sim_d": ("Your child solves a puzzle step by step and sees the result right away. The regular course doesn't have simulators.",
              "Anak memecahkan teka-teki langkah demi langkah dan langsung melihat hasilnya. Kursus reguler tidak memiliki simulator."),
    "sim1": ("Put the steps in order: help the astro-cadet cook noodles", "Susun langkah: bantu astrokadet memasak mi"),
    "sim2": ("Write a program: lead the Mars bot to the flag", "Susun program: antar Bot Mars sampai ke bendera"),
    "sim3": ("Split a long path into checkpoints", "Bagi jalur panjang menjadi checkpoint"),
    "dc_h3": ("Questions go to Discord", "Pertanyaan diajukan di Discord"),
    "dc_d": ("A moderator answers first, 12:00–20:00 WIB. When a task is tricky, a tutor joins and explains.",
             "Moderator menjawab lebih dulu, pukul 12:00–20:00 WIB. Kalau tugasnya sulit, tutor ikut membantu dan menjelaskan."),
    "cap_dc": ("Example chat in Discord", "Contoh obrolan di Discord"),
    # reports
    "r_eyebrow": ("Reports for parents", "Laporan untuk orang tua"),
    "r_h2": ("You see progress every week", "Anda melihat perkembangan setiap minggu"),
    "r1t": ("Every week · WhatsApp", "Setiap minggu · WhatsApp"),
    "r1d": ("A short message: what your child did and what's next.", "Pesan singkat: apa yang sudah dikerjakan anak dan apa selanjutnya."),
    "r2t": ("Every 3 weeks · PDF", "Setiap 3 minggu · PDF"),
    "r2d": ("A cycle report with the project and the tutor's comment.", "Laporan siklus berisi proyek dan komentar tutor."),
    "cap_wa": ("Weekly message in WhatsApp", "Pesan mingguan di WhatsApp"),
    "cap_pdf": ("Example cycle report", "Contoh laporan siklus"),
    "open_full": ("Open full size", "Buka ukuran penuh"),
    # how it works
    "hw_eyebrow": ("How it works", "Cara kerjanya"),
    "hw_h2": ("Learn at home at your own pace.<br>Support in the chat every day.<br>Live meeting every 3 weeks.",
              "Belajar di rumah sesuai ritme sendiri.<br>Bantuan di chat setiap hari.<br>Pertemuan live setiap 3 minggu."),
    "s0e": ("After payment", "Setelah pembayaran"),
    "s0t": ("Welcome meeting and onboarding", "Pertemuan perkenalan dan orientasi"),
    "s0d": ("Your child meets the tutor and the group, then does the first onboarding tasks on the learning platform.",
            "Anak berkenalan dengan tutor dan grup, lalu mengerjakan tugas orientasi pertama di platform belajar."),
    "s1e": ("Every week", "Setiap minggu"),
    "s1t": ("At home: one lesson", "Di rumah: satu pelajaran"),
    "s1d": ("3–5 short parts of 15–20 min: video, quiz, simulator, Scratch tasks. Questions go to Discord.",
            "3–5 bagian singkat 15–20 menit: video, kuis, simulator, tugas Scratch. Pertanyaan diajukan di Discord."),
    "s2e": ("Every 3 weeks", "Setiap 3 minggu"),
    "s2t": ("Live meeting", "Pertemuan live"),
    "s2d": ("90 minutes with the tutor in a group of 4: show projects, fix bugs, a group challenge.",
            "90 menit bersama tutor dalam grup 4 anak: tunjukkan proyek, perbaiki bug, tantangan grup."),
    "s3e": ("Every week &amp; 3 weeks", "Setiap minggu &amp; 3 minggu"),
    "s3t": ("Report", "Laporan"),
    "s3d": ("Every week: what your child did and what's next. Every 3 weeks: a PDF report with the project and the tutor's comment.",
            "Setiap minggu: apa yang sudah dikerjakan anak dan apa selanjutnya. Setiap 3 minggu: laporan PDF berisi proyek dan komentar tutor."),
    "repeat": ("Steps 1–3 repeat <b>12 times</b> over the course", "Langkah 1–3 diulang <b>12 kali</b> selama kursus"),
    "pc_t": ("You need a computer or laptop", "Perlu komputer atau laptop"),
    "pc_d": ("Scratch doesn't work on a phone. Please check this before the course starts.",
             "Scratch tidak bisa dijalankan di ponsel. Mohon pastikan ini sebelum kursus dimulai."),
    "role_t": ("Parent's role", "Peran orang tua"),
    "role_d": ("Help your child keep a regular rhythm. We support you with reminders and reports.",
               "Bantu anak menjaga ritme belajar yang teratur. Kami mendukung Anda dengan pengingat dan laporan."),
    # comparison
    "cmp_eyebrow": ("Comparison", "Perbandingan"),
    "cmp_h2": ("Same course. More support. Lower price.", "Kursus yang sama. Dukungan lebih banyak. Harga lebih murah."),
    "cmp_feature": ("Feature", "Fitur"),
    "cmp_reg": ("Regular format", "Format reguler"),
    "cmp_reg_s": ("Regular", "Reguler"),
    "cmp_flex_s": ("Flexible", "Fleksibel"),
    "cmp_flex": ("Flexible format", "Format fleksibel"),
    "best": ("<strong>Best for</strong> busy families, kids who like their own pace, and parents who want to see progress every week.",
             "<strong>Paling cocok untuk</strong> keluarga yang sibuk, anak yang suka belajar sesuai ritmenya sendiri, dan orang tua yang ingin melihat perkembangan setiap minggu."),
    # kevin
    "k_h2": ("Tutor explains the flexible format in 50 seconds", "Tutor menjelaskan format fleksibel dalam 50 detik"),
    # expandable details
    "more_h3": ("See how it works <span class=\"muted\" style=\"font-weight:400\">(click to expand)</span>", "Lihat cara kerjanya <span class=\"muted\" style=\"font-weight:400\">(klik untuk membuka)</span>"),
    "acc_lesson_t": ("Inside a lesson", "Isi satu pelajaran"),
    "acc_lesson_d": ("3–5 short parts: video, quiz, simulator, Scratch tasks", "3–5 bagian singkat: video, kuis, simulator, tugas Scratch"),
    "acc_sim_d": ("Our main new feature: a puzzle before the code", "Fitur baru utama: teka-teki sebelum kode"),
    "acc_dc_t": ("Questions in Discord", "Pertanyaan di Discord"),
    "acc_dc_d": ("A moderator answers first, tutors help with harder tasks", "Moderator menjawab lebih dulu, tutor membantu tugas yang sulit"),
    "show": ("Show", "Lihat"),
    "hide": ("Hide", "Tutup"),
    "see_lesson": ("See inside a lesson", "Lihat isi pelajaran"),
    "see_sim": ("See the simulators", "Lihat simulatornya"),
    "see_example": ("See an example", "Lihat contoh"),
    "k_d": ("Kevin teaches Visual Programming at Algonova and records the video lessons.",
            "Kevin adalah guru Pemrograman Visual di Algonova dan merekam video pelajarannya."),
    "k_note": ("The video is in Bahasa Indonesia.", ""),
    "cap_kevin": ("Kevin, Visual Programming teacher · 50 sec", "Kevin, guru Pemrograman Visual · 50 detik"),
    # course + cta + footer
    "about_eyebrow": ("About the course", "Tentang kursus"),
    "about_h2": ("Want a reminder of what your child learns?", "Ingin melihat lagi apa yang dipelajari anak?"),
    "about_d": ("See the Visual Programming program: topics, modules and the projects your child builds.",
                "Lihat program Pemrograman Visual: topik, modul, dan proyek yang dibuat anak."),
    "about_btn": ("Visual Programming course", "Kursus Pemrograman Visual"),
    "cta_h2": ("Ready to start?", "Siap memulai?"),
    "cta_d": ("Message us on WhatsApp — the message <strong>“I’m interested. I want to buy Flexible format.”</strong> is ready to send, and we’ll get your child started.",
              "Hubungi kami di WhatsApp — pesan <strong>“Saya tertarik. Saya ingin membeli format Fleksibel.”</strong> sudah siap dikirim, dan kami akan membantu anak Anda mulai belajar."),
    "cta_btn": ("Message us on WhatsApp", "Hubungi kami di WhatsApp"),
    "f_contact": ("Contact", "Kontak"),
    "f_email": ("Email", "Email"),
    "f_rights": ("All rights reserved 2026", "Hak cipta dilindungi undang-undang 2026"),
    "f_main": ("https://algonova.com/ind/en", "https://algonova.com/ind/id"),
    "foot": ("International online IT school for kids and teens, 5–17", "Sekolah IT online internasional untuk anak dan remaja usia 5–17 tahun"),
    # meetings page
    "m_title": ("12 live meetings — Visual Programming Flexible Format | Algonova", "12 pertemuan live — Pemrograman Visual Format Fleksibel | Algonova"),
    "m_desc": ("All 12 live meetings of the Visual Programming flexible format: one every 3 weeks, 90 minutes, groups of 4.",
               "Semua 12 pertemuan live Pemrograman Visual format fleksibel: setiap 3 minggu, 90 menit, grup 4 anak."),
    "m_back": ("Back to the flexible format", "Kembali ke format fleksibel"),
    "m_eyebrow": ("Visual Programming · Flexible format", "Pemrograman Visual · Format fleksibel"),
    "m_h1a": ("12 live meetings.", "12 pertemuan live."),
    "m_h1b": ("One every 3 weeks.", "Setiap 3 minggu."),
    "m_lead": ("Every 3 weeks the group meets the tutor in Zoom to show projects and do a fun challenge together.",
               "Setiap 3 minggu, grup bertemu tutor di Zoom untuk menunjukkan proyek dan mengerjakan tantangan seru bersama."),
    "m_f1": ("<b>90</b> minutes", "<b>90</b> menit"),
    "m_f2": ("Groups of <b>4</b> kids", "Grup <b>4</b> anak"),
    "m_f3": ("Friday–Sunday", "Jumat–Minggu"),
    "m_f4": ("Recorded, if your child misses it", "Direkam, kalau anak berhalangan"),
    "m_plan": ("All meetings of the course", "Semua pertemuan kursus"),
    "m_w0t": ("Welcome meeting", "Pertemuan perkenalan"),
    "m_w0d": ("Before the start: meet the tutor and the group, then first onboarding tasks on the platform.",
              "Sebelum mulai: kenalan dengan tutor dan grup, lalu tugas orientasi pertama di platform."),
    "m_module": ("Module", "Modul"),
    "m_weeks": ("Weeks", "Minggu"),
    "m_exH": ("Example: meeting 1 · Dance battle", "Contoh: pertemuan 1 · Battle Tari"),
    "m_exN": ("Example plan, the tutor adapts it to the group.", "Contoh rencana, tutor menyesuaikannya dengan grup."),
    "m_min": ("min", "menit"),
    "m_foot": ("36 weeks · 7 modules · 12 meetings + a welcome meeting. Exact dates and time slots are set when the group is complete.",
               "36 minggu · 7 modul · 12 pertemuan + pertemuan perkenalan. Tanggal dan jam pasti ditentukan setelah grup terisi."),
}

# comparison rows: label, regular(long, short), flexible(long, short), flexible is a plus?
CMP = [
    ((("Price per lesson", "Price"), ("Harga per pelajaran", "Harga")),
     (("Regular price", "Regular"), ("Harga reguler", "Reguler")),
     (("3× cheaper", "3× cheaper"), ("3× lebih murah", "3× lebih murah")), "price"),
    ((("Theory", "Theory"), ("Teori", "Teori")),
     (("Explained only in the live lesson", "Only live"), ("Dijelaskan hanya di kelas live", "Hanya di kelas live")),
     (("Video in every lesson, rewatch anytime", "Video, rewatch anytime"), ("Video di setiap pelajaran, bisa ditonton ulang kapan saja", "Video, bisa diulang")), "plus"),
    ((("Simulators", "Simulators"), ("Simulator", "Simulator")),
     (("No simulators", "—"), ("Tidak ada simulator", "—")),
     (("New: interactive puzzles in every lesson", "In every lesson"), ("Baru: teka-teki interaktif di setiap pelajaran", "Di setiap pelajaran")), "plus"),
    ((("Support between lessons", "Daily support"), ("Bantuan di antara kelas", "Bantuan harian")),
     (("No daily support", "No daily chat"), ("Tidak ada bantuan harian", "Tidak ada chat harian")),
     (("Discord chat every day, 12:00–20:00 WIB", "Daily, 12:00–20:00"), ("Chat Discord setiap hari, 12:00–20:00 WIB", "Setiap hari, 12:00–20:00")), "plus"),
    ((("Report to parent", "Reports"), ("Laporan untuk orang tua", "Laporan")),
     (("Once a month", "Monthly"), ("Sebulan sekali", "Bulanan")),
     (("Every week + a PDF report every 3 weeks", "Weekly + PDF"), ("Setiap minggu + laporan PDF setiap 3 minggu", "Mingguan + PDF")), "plus"),
    ((("Missed lesson", "Missed lesson"), ("Kelas terlewat", "Kelas terlewat")),
     (("Make-up or lost", "Make-up or lost"), ("Kelas pengganti atau hangus", "Diganti atau hangus")),
     (("Recorded, always available", "Recorded"), ("Terekam, selalu tersedia", "Terekam")), "plus"),
    ((("Pace", "Pace"), ("Ritme belajar", "Ritme belajar")),
     (("Fixed weekly schedule", "Fixed schedule"), ("Jadwal mingguan tetap", "Jadwal tetap")),
     (("Your child's own pace", "Own pace"), ("Sesuai ritme anak", "Ritme anak")), "plus"),
    ((("36 topics and certificate", "Topics & certificate"), ("36 topik dan sertifikat", "Topik & sertifikat")),
     (("Yes", "Yes"), ("Ya", "Ya")),
     (("Same", "Same"), ("Sama", "Sama")), "plus"),
    ((("Live lessons with a tutor", "Live with a tutor"), ("Kelas live bersama tutor", "Kelas live")),
     (("Every week", "Every week"), ("Setiap minggu", "Setiap minggu")),
     (("Every 3 weeks", "Every 3 weeks"), ("Setiap 3 minggu", "Setiap 3 minggu")), "neutral"),
]

MODS = [
    (("Introduction", "Pengenalan"), [
        (1, ("Dance battle", "Battle Tari"), ("Everyone's dances in one group clip.", "Tarian semua teman jadi satu klip.")),
        (2, ("Living name card", "Kartu nama hidup"), ("Show your card, swap with a friend.", "Tunjukkan kartumu, bertukar dengan teman."))]),
    (("Movement and messages", "Gerak dan pesan"), [
        (3, ("Treasure map", "Peta harta karun"), ("Find a friend's treasure with coordinates.", "Temukan harta teman dengan koordinat.")),
        (4, ("Cartoon relay", "Estafet kartun"), ("Everyone's scenes in one cartoon.", "Adegan semua teman jadi satu kartun."))]),
    (("Games", "Game"), [
        (5, ("Maze race", "Balapan labirin"), ("Steer through a maze with the arrow keys.", "Lewati labirin dengan tombol panah.")),
        (6, ("Game fair", "Pameran game"), ("Halfway! Friends and parents play your game.", "Setengah jalan! Teman dan orang tua main game-mu."))]),
    (("Logic", "Logika"), [
        (7, ("Crack the safe", "Bobol brankas"), ("A friend tries to crack your code.", "Teman mencoba menebak kodemu.")),
        (8, ("Shared Mars map", "Peta Mars bersama"), ("Everyone's zones in one Mars world.", "Zona semua teman jadi satu dunia Mars."))]),
    (("Variables", "Variabel"), [
        (9, ("Clicker tournament", "Turnamen clicker"), ("Score, timer and a leaderboard.", "Skor, timer, dan papan peringkat.")),
        (10, ("Chatbot show", "Pertunjukan chatbot"), ("Friends chat with your bot.", "Teman mengobrol dengan bot-mu."))]),
    (("Clones", "Klon"), [
        (11, ("Clone arcade", "Arkade klon"), ("A Flappy Bird–style game with clones.", "Game bergaya Flappy Bird dengan klon."))]),
    (("Final project", "Proyek akhir"), [
        (12, ("Demo day", "Demo day"), ("Final projects for parents, certificates.", "Proyek akhir untuk orang tua, sertifikat."))]),
]
EX = [((0, 10), ("Warm-up", "Pemanasan"), ("Quick quiz", "Kuis singkat")),
      ((10, 30), ("Show projects", "Tunjukkan proyek"), ("Each kid shows their dance", "Setiap anak menunjukkan tariannya")),
      ((30, 45), ("Fix bugs", "Perbaiki bug"), ("Common mistakes", "Kesalahan umum")),
      ((45, 80), ("Dance battle", "Battle Tari"), ("All dances in one clip", "Semua tarian jadi satu klip")),
      ((80, 90), ("Wrap-up", "Penutup"), ("Best move vote", "Voting gerakan terbaik"))]

# ------------------------------------------------------------------ icons (inline, currentColor)
def svg(body, size=24, fill="none"):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="{fill}" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{body}</svg>')

I = {
    "play": lambda s=24: svg('<polygon points="7 4 20 12 7 20 7 4" fill="currentColor"></polygon>', s),
    "screen": lambda s=24: svg('<rect x="3" y="4" width="18" height="12" rx="2"></rect><path d="M8 20l4-4 4 4"></path>', s),
    "chat": lambda s=24: svg('<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1.1-4.6A8 8 0 1 1 21 12z"></path>', s),
    "check": lambda s=24: svg('<circle cx="12" cy="12" r="9"></circle><path d="M8 12.5l2.5 2.5L16 9.5"></path>', s),
    "trophy": lambda s=24: svg('<path d="M8 4h8v5a4 4 0 0 1-8 0V4zM8 6H5a3 3 0 0 0 3 4M16 6h3a3 3 0 0 1-3 4M12 13v4M8 20h8"></path>', s),
    "puzzle": lambda s=24: svg('<path d="M10 3h4v3a2 2 0 1 0 4 0V3h3v7h-3a2 2 0 1 0 0 4h3v7h-7v-3a2 2 0 1 0-4 0v3H3v-7h3a2 2 0 1 0 0-4H3V3h7z"></path>', s),
    "quiz": lambda s=24: svg('<circle cx="12" cy="12" r="9"></circle><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6V14"></path><path d="M12 17.5h.01"></path>', s),
    "blocks": lambda s=24: svg('<rect x="3" y="4" width="10" height="6" rx="1"></rect><rect x="7" y="14" width="14" height="6" rx="1"></rect><path d="M8 10v4"></path>', s),
    "doc": lambda s=24: svg('<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"></path><path d="M14 3v5h5M9 13h6M9 17h6"></path>', s),
    "cal": lambda s=24: svg('<rect x="3" y="5" width="18" height="16" rx="2"></rect><path d="M3 10h18M8 3v4M16 3v4"></path>', s),
    "laptop": lambda s=24: svg('<rect x="4" y="5" width="16" height="11" rx="1"></rect><path d="M2 19h20"></path>', s),
    "arrow": lambda s=24: svg('<path d="M5 12h14M13 6l6 6-6 6"></path>', s),
    "back": lambda s=24: svg('<path d="M19 12H5M11 6l-6 6 6 6"></path>', s),
    "wa": lambda s=24: f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/></svg>',
    "plus": lambda s=24: svg('<path d="M5 12.5l4.5 4.5L19 7.5"></path>', s),
}

CSS = r"""
:root{
  --background:#FFFFFF; --foreground:#101828; --canvas:#F7F7F8;
  --card:#FFFFFF; --muted:#F2F2F3; --muted-foreground:#4A4A55;
  --primary:#5800E5; --primary-hover:#3900AD; --primary-foreground:#FFFFFF;
  --primary-subtle:#F1EBFE; --secondary:#F1EBFE; --secondary-foreground:#3900AD;
  --border:#E2E2E6; --ring:#B299FF; --surface-hover:#ECECEF;
  --warning-subtle:#FDF3E2; --warning-text:#8A5D00;
  --lime:#D9FF00; --violet:#B299FF; --on-lime:#101828;
  --chip:#DCCEFE; --chip-foreground:#2E008A;
  --hero:#101828;
  --on-dark:#FFFFFF; --on-dark-muted:rgba(255,255,255,.78); --on-dark-fill:rgba(255,255,255,.08); --on-dark-hover:rgba(255,255,255,.16);
  --on-primary-muted:rgba(255,255,255,.86); --on-primary-fill:rgba(255,255,255,.14);
  --wa:#075E54; --wa-hover:#054A42;
  --radius-xs:2px; --radius-sm:4px; --radius-md:8px; --radius-lg:12px; --radius-xl:16px; --radius-pill:999px;
  --shadow-e2:0 1px 2px rgba(16,24,40,.03),0 3px 10px rgba(16,24,40,.04);
  --shadow-e3:0 2px 6px rgba(16,24,40,.05),0 12px 32px rgba(16,24,40,.08);
  --dur:.18s; --ease:cubic-bezier(.2,.6,.3,1);
}
*{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--background);color:var(--foreground);font:400 16px/1.5 Inter,system-ui,-apple-system,"Segoe UI",sans-serif;-webkit-font-smoothing:antialiased;overflow-x:hidden}
img,video{display:block;max-width:100%;height:auto}
h1,h2,h3,p,figure{margin:0}
a{color:var(--primary)}
a:focus-visible,button:focus-visible,video:focus-visible{outline:2px solid var(--ring);outline-offset:2px;border-radius:var(--radius-sm)}
.wrap{max-width:1200px;margin:0 auto;padding:0 24px}
.sec{padding:96px 0}
.bg-canvas{background:var(--canvas)}
.stack{display:flex;flex-direction:column}
.head{display:flex;flex-direction:column;gap:12px;max-width:800px}
.eyebrow{font-size:12px;line-height:16px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--primary)}
h1{font-size:48px;line-height:1.05;letter-spacing:-.03em;font-weight:700}
h2{font-size:32px;line-height:1.15;letter-spacing:-.02em;font-weight:700}
h3{font-size:20px;line-height:1.3;letter-spacing:-.01em;font-weight:700}
.lead{font-size:20px;line-height:1.5;color:var(--muted-foreground)}
.muted{color:var(--muted-foreground)}
.small{font-size:12px;line-height:16px}
.tnum{font-variant-numeric:tabular-nums}

/* buttons */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:48px;padding:12px 24px;border-radius:var(--radius-md);font:600 16px/1.2 Inter,system-ui,sans-serif;text-decoration:none;transition:background var(--dur) var(--ease),color var(--dur) var(--ease)}
.btn:active{transform:translateY(1px)}
.btn-primary{background:var(--primary);color:var(--primary-foreground)}
.btn-primary:hover{background:var(--primary-hover);color:var(--primary-foreground)}
.btn-light{background:var(--background);color:var(--foreground)}
.btn-light:hover{background:var(--surface-hover);color:var(--foreground)}
.btn-secondary{background:var(--secondary);color:var(--secondary-foreground)}
.btn-secondary:hover{background:var(--chip);color:var(--chip-foreground)}
.btn-wa{background:var(--wa);color:var(--primary-foreground)}
.btn-wa:hover{background:var(--wa-hover);color:var(--primary-foreground)}
.link{display:inline-flex;align-items:center;gap:8px;min-height:44px;font-weight:600;text-decoration:none;color:var(--primary)}
.link:hover{text-decoration:underline;text-underline-offset:4px}
.on-primary .link{color:var(--primary-foreground)}

/* hero / dark header */
.hero{background:var(--hero);color:var(--on-dark);padding:24px 0 96px}
.nav{display:flex;align-items:center;justify-content:space-between;gap:16px}
.nav img{height:32px;width:auto;flex:none}
.nav-right{display:flex;align-items:center;gap:20px;min-width:0}
.nav-tag{font-size:16px;font-weight:500;color:var(--on-dark-muted)}
.lang{display:inline-flex;gap:4px;padding:4px;border-radius:var(--radius-pill);background:var(--on-dark-fill)}
.lang a,.lang span{display:inline-flex;align-items:center;justify-content:center;min-width:44px;min-height:40px;padding:0 12px;border-radius:var(--radius-pill);font-size:12px;font-weight:700;letter-spacing:.06em;text-decoration:none}
.lang span{background:var(--background);color:var(--foreground)}
.lang a{color:var(--on-dark-muted)}
.lang a:hover{background:var(--on-dark-hover);color:var(--on-dark)}
.hero-grid{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(0,1fr);gap:56px;align-items:center;margin-top:72px}
.hero .eyebrow{color:var(--violet)}
.hero h1 .mark{background:var(--lime);color:var(--on-lime);padding:0 8px;border-radius:var(--radius-sm);-webkit-box-decoration-break:clone;box-decoration-break:clone}
.hero .lead{color:var(--on-dark-muted);max-width:620px}
.hero .lead strong{color:var(--on-dark)}
.hero-copy{display:flex;flex-direction:column;gap:24px}
.btns{display:flex;flex-wrap:wrap;gap:12px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin:0;padding:0;list-style:none}
.chip{display:inline-flex;align-items:center;gap:8px;padding:8px 16px;border-radius:var(--radius-pill);background:var(--on-dark-fill);font-weight:500}
.chip svg{color:var(--violet)}
.stat{position:relative;background:var(--background);color:var(--foreground);border-radius:var(--radius-xl);padding:32px;display:flex;flex-direction:column;gap:8px;box-shadow:var(--shadow-e3)}
.stat .num{display:flex;align-items:baseline;gap:12px}
.stat .num b{font-size:48px;line-height:1;letter-spacing:-.04em;color:var(--primary)}
.stat .num span{font-size:24px;font-weight:700}
.sticker{position:absolute;top:-40px;right:-8px;width:128px;transform:rotate(8deg);filter:drop-shadow(0 6px 14px rgba(16,24,40,.18))}

/* cards */
.grid3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.card{background:var(--canvas);border-radius:var(--radius-lg);padding:24px;display:flex;flex-direction:column;gap:12px}
.bg-canvas .card{background:var(--card);box-shadow:var(--shadow-e2)}
.card p{color:var(--muted-foreground)}
.card.on-primary{background:var(--primary);color:var(--primary-foreground)}
.card.on-primary p{color:var(--on-primary-muted)}
.ico{width:48px;height:48px;border-radius:var(--radius-md);background:var(--background);color:var(--primary);display:inline-flex;align-items:center;justify-content:center;flex:none}
.bg-canvas .ico{background:var(--primary-subtle)}
.on-primary .ico{background:var(--on-primary-fill);color:var(--primary-foreground)}
.card-top{display:flex;align-items:center;justify-content:space-between;gap:12px}
.badge{display:inline-flex;align-items:center;padding:4px 8px;border-radius:var(--radius-pill);background:var(--chip);color:var(--chip-foreground);font-size:12px;line-height:16px;font-weight:700;letter-spacing:.06em;text-transform:uppercase}
.total{display:flex;align-items:center;gap:12px;color:var(--muted-foreground)}
.total svg{color:var(--primary);flex:none}
.total b{color:var(--foreground)}

/* media */
.fig{background:var(--card);border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow-e2);display:flex;flex-direction:column}
.fig video,.fig img{width:100%;background:var(--muted)}
.fig figcaption{padding:12px 16px;color:var(--muted-foreground)}
.fig.flat{box-shadow:none;background:var(--canvas)}
.fig a.zoom{display:block}
.split{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px;align-items:start}
.parts{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}
.part{background:var(--card);border-radius:var(--radius-lg);box-shadow:var(--shadow-e2);padding:20px;display:flex;flex-direction:column;gap:8px}
.part .ico{width:40px;height:40px;background:var(--primary-subtle)}
.part p{color:var(--muted-foreground)}
.panel{background:var(--card);border-radius:var(--radius-xl);box-shadow:var(--shadow-e2);padding:32px;display:flex;flex-direction:column;gap:24px}
.panel-head{display:flex;flex-direction:column;gap:8px;max-width:720px}
.panel-head .row{display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.panel .grid3{gap:16px}
.dc{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.6fr);gap:32px;align-items:center}

/* reports */
.rep{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.1fr);gap:48px;align-items:center}
.rep-items{display:flex;flex-direction:column;gap:16px}
.rep-item{background:var(--canvas);border-radius:var(--radius-lg);padding:24px;display:flex;gap:16px;align-items:flex-start}
.bg-canvas .rep-item{background:var(--card);box-shadow:var(--shadow-e2)}
.rep-item p{color:var(--muted-foreground)}
.rep-media{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;align-items:start}
.rep-media img{aspect-ratio:18/25;object-fit:cover;object-position:top}

/* steps */
.steps{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}
.step{background:var(--canvas);border-radius:var(--radius-lg);padding:24px;display:flex;flex-direction:column;gap:8px}
.bg-canvas .step{background:var(--card);box-shadow:var(--shadow-e2)}

/* expandable details */
.more{display:flex;flex-direction:column;gap:12px}
.acc{background:var(--canvas);border-radius:var(--radius-lg);scroll-margin-top:16px}
.acc summary{list-style:none;cursor:pointer;display:flex;align-items:center;gap:16px;padding:16px 20px;min-height:80px;border-radius:var(--radius-lg);transition:background var(--dur) var(--ease)}
.acc summary::-webkit-details-marker{display:none}
.acc summary:hover{background:var(--surface-hover)}
.acc summary:focus-visible{outline:2px solid var(--ring);outline-offset:2px}
.acc[open] summary{border-radius:var(--radius-lg) var(--radius-lg) 0 0}
.acc .sm{display:flex;flex-direction:column;gap:4px;flex:1;min-width:0}
.acc .sm b{font-size:20px;line-height:1.3;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.acc .sm span{color:var(--muted-foreground)}
.acc .act{display:inline-flex;align-items:center;gap:8px;color:var(--primary);font-weight:600;flex:none}
.acc .act svg{transition:transform var(--dur) var(--ease)}
.acc[open] .act svg{transform:rotate(90deg)}
.acc .o2,.acc[open] .o1{display:none}
.acc[open] .o2{display:inline}
.acc-body{padding:8px 20px 24px;display:flex;flex-direction:column;gap:20px}
.step .n{width:40px;height:40px;border-radius:var(--radius-pill);background:var(--primary);color:var(--primary-foreground);display:inline-flex;align-items:center;justify-content:center;font-weight:700;margin-bottom:8px}
.step .e{font-size:12px;line-height:16px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--primary)}
.step p{color:var(--muted-foreground)}
.step.on-primary{background:var(--primary);color:var(--primary-foreground)}
.step.on-primary .n{background:var(--lime);color:var(--on-lime)}
.step.on-primary .e{color:var(--violet)}
.step.on-primary p{color:var(--on-primary-muted)}
.callouts{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
.callout{border-radius:var(--radius-lg);padding:20px 24px;display:flex;gap:16px;align-items:flex-start}
.callout.warn{background:var(--warning-subtle)}
.callout.warn svg{color:var(--warning-text)}
.callout.warn b{color:var(--warning-text)}
.callout.role{background:var(--primary-subtle)}
.callout.role svg,.callout.role b{color:var(--primary)}
.callout svg{flex:none;margin-top:2px}

/* comparison */
.cmp{background:var(--canvas);border-radius:var(--radius-xl);overflow:hidden}
.cmp table{width:100%;border-collapse:collapse}
.cmp th,.cmp td{text-align:left;vertical-align:top;padding:16px 24px}
.cmp thead th{font-size:12px;line-height:16px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--muted-foreground);padding-top:20px;padding-bottom:20px}
.cmp thead th.flex{background:var(--primary);color:var(--primary-foreground)}
.cmp tbody tr{border-top:1px solid var(--border)}
.cmp tbody th{font-weight:600;width:30%}
.cmp td.reg{color:var(--muted-foreground);width:32%}
.cmp td.flex{background:var(--secondary);font-weight:600}
.cmp td.flex .ok{color:var(--primary);margin-right:4px}
.cmp td.price{color:var(--primary);font-size:24px;line-height:1.2;font-weight:700}
.cmp td.neutral{font-weight:400;color:var(--muted-foreground)}
.cmp .s{display:none}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}

/* kevin */
.kev{display:flex;flex-direction:column;align-items:center;gap:32px;text-align:center}
.kev h2{max-width:720px}
.kev-video{width:100%;max-width:960px;border-radius:var(--radius-xl);box-shadow:var(--shadow-e3);background:var(--hero)}

/* course + cta */
.box{border-radius:var(--radius-xl);padding:48px;display:flex;flex-wrap:wrap;gap:32px;align-items:center;justify-content:space-between}
.box.canvas{background:var(--canvas)}
.box.violet{background:var(--primary);color:var(--primary-foreground)}
.box .txt{flex:1 1 480px;display:flex;flex-direction:column;gap:12px}
.box.violet p{color:var(--on-primary-muted)}
.box.violet strong{color:var(--primary-foreground)}
.foot{background:var(--hero);color:var(--on-dark-muted);padding:48px 0}
.foot img{height:32px;width:auto;align-self:flex-start}
.foot-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:40px;align-items:start}
.foot-h{color:var(--on-dark-muted)}
.foot a{color:var(--on-dark);text-decoration:none;align-self:flex-start;min-height:28px}
.foot a:hover{text-decoration:underline;text-underline-offset:4px}
.foot a.main{color:var(--violet);font-weight:600}
.socials{display:flex;gap:8px}
.foot .socials a{width:44px;height:44px;display:inline-flex;align-items:center;justify-content:center;border-radius:var(--radius-md);background:var(--on-dark-fill);color:var(--on-dark)}
.foot .socials a:hover{background:var(--on-dark-hover);text-decoration:none}

/* meetings page */
.back{display:inline-flex;align-items:center;gap:8px;min-height:44px;color:var(--on-dark-muted);text-decoration:none;font-weight:600;margin-top:40px}
.back:hover{color:var(--on-dark)}
.hero-sm{padding-bottom:64px}
.hero-sm .hero-copy{margin-top:24px;max-width:820px}
.hero .hl{color:var(--violet)}
.facts{display:flex;flex-wrap:wrap;gap:8px;margin:0;padding:0;list-style:none}
.facts li{padding:8px 16px;border-radius:var(--radius-pill);background:var(--on-dark-fill);font-weight:500}
.facts b{color:var(--violet)}
.w0{display:flex;gap:16px;align-items:center;background:var(--lime);color:var(--on-lime);border-radius:var(--radius-lg);padding:20px 24px}
.w0 .z{font-size:32px;line-height:1;font-weight:700;min-width:40px}
.mods{display:flex;flex-direction:column;gap:32px}
.mod{display:grid;grid-template-columns:200px minmax(0,1fr);gap:24px;align-items:start}
.mod .m{font-size:12px;line-height:16px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--muted-foreground)}
.mod .nm{font-size:20px;font-weight:700;line-height:1.3}
.mcards{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
.mcards.one{grid-template-columns:minmax(0,1fr)}
.mcard{background:var(--card);border-radius:var(--radius-lg);box-shadow:var(--shadow-e2);padding:20px 24px;display:flex;flex-direction:column;gap:8px}
.mcard .row{display:flex;align-items:center;gap:12px}
.mcard .b{min-width:36px;height:36px;border-radius:var(--radius-md);background:var(--primary);color:var(--primary-foreground);display:inline-flex;align-items:center;justify-content:center;font-weight:700}
.mcard.final .b{background:var(--primary-subtle);color:var(--primary)}
.mcard p{color:var(--muted-foreground)}
.ruler{display:grid;grid-template-columns:repeat(36,minmax(0,1fr));gap:2px;margin-top:4px}
.ruler i{height:4px;border-radius:var(--radius-xs);background:var(--border)}
.ruler i.on{background:var(--primary)}
.bar{display:flex;gap:4px}
.seg{min-width:0;border-radius:var(--radius-md);padding:12px;background:var(--primary-subtle);display:flex;flex-direction:column;gap:4px}
.seg.hot{background:var(--primary);color:var(--primary-foreground)}
.seg .min{font-size:12px;line-height:16px;font-weight:700}
.seg .t{font-weight:700;line-height:1.25}
.seg .d{color:var(--muted-foreground);line-height:1.35}
.seg.hot .d{color:var(--on-primary-muted)}
.scale{display:flex;justify-content:space-between;font-size:12px;color:var(--muted-foreground);margin-top:8px}

@media (max-width:1024px){
  .grid3{grid-template-columns:repeat(2,minmax(0,1fr))}
  .steps{grid-template-columns:repeat(2,minmax(0,1fr))}
  .parts{grid-template-columns:repeat(2,minmax(0,1fr))}
  .hero-grid,.rep,.dc{grid-template-columns:minmax(0,1fr);gap:40px}
  .hero-grid .stat{max-width:480px}
}
@media (max-width:767px){
  .wrap{padding:0 16px}
  .sec{padding:64px 0}
  h1{font-size:32px;line-height:1.1}
  h2{font-size:28px}
  .lead{font-size:16px}
  .hero{padding-bottom:64px}
  .hero-grid{margin-top:40px}
  .nav-tag{display:none}
  .hero .chips,.hero-grid .stat{display:none}
  .lang a,.lang span{min-height:44px}
  .btns .btn{flex:1 1 100%}
  .grid3,.steps,.split,.callouts,.panel .grid3{grid-template-columns:minmax(0,1fr)}
  .parts{gap:12px}
  .part{padding:16px}
  .panel{padding:20px;gap:20px}
  .sticker{width:96px;top:-32px}
  .stat{padding:24px}
  .box{padding:28px 20px}
  .box .btn{flex:1 1 100%}
  .rep-media{gap:12px}
  .acc summary{padding:16px;gap:12px}
  .acc .act .o1,.acc[open] .act .o2{display:none}
  .acc-body{padding:4px 12px 16px}
  .rep-item{padding:20px}
  /* comparison: compact 3-column table, fits the phone width */
  .cmp .l{display:none}
  .cmp .s{display:inline}
  .cmp table{table-layout:fixed}
  .cmp th,.cmp td{padding:12px 8px;font-size:14px;line-height:1.3}
  .cmp thead th{font-size:12px;letter-spacing:.04em;padding:14px 8px}
  .cmp thead th:first-child,.cmp tbody th{width:31%;padding-left:12px}
  .cmp tbody th{font-weight:700;color:var(--foreground)}
  .cmp td.reg{width:31%}
  .cmp td.flex .ok{margin-right:2px}
  .cmp td.price{font-size:16px}
  .foot-grid{grid-template-columns:minmax(0,1fr);gap:32px}
  .mod{grid-template-columns:minmax(0,1fr);gap:12px}
  .mcards{grid-template-columns:minmax(0,1fr)}
  .bar{flex-direction:column}
  .seg{flex:none!important}
  .scale{display:none}
}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}.btn{transition:none}}
"""

JS = r"""
(function(){
  function openFrom(hash){if(!hash||hash.indexOf('#more-')!==0)return;var d=document.querySelector(hash);if(d&&d.tagName==='DETAILS')d.open=true;}
  [].slice.call(document.querySelectorAll('a[href^="#more-"]')).forEach(function(a){a.addEventListener('click',function(){openFrom(a.getAttribute('href'));});});
  openFrom(location.hash);
})();
(function(){
  var vids=[].slice.call(document.querySelectorAll('video.loop'));
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(reduce){vids.forEach(function(v){v.removeAttribute('autoplay');v.controls=true;});return;}
  if(!('IntersectionObserver' in window)){vids.forEach(function(v){v.play&&v.play().catch(function(){});});return;}
  var io=new IntersectionObserver(function(es){es.forEach(function(e){var v=e.target;
    if(e.isIntersecting){if(v.preload==='none'){v.preload='auto';}var p=v.play();if(p&&p.catch)p.catch(function(){v.controls=true;});}
    else{v.pause();}});},{rootMargin:'200px 0px',threshold:0.01});
  vids.forEach(function(v){io.observe(v);});
})();
"""


# ------------------------------------------------------------------ helpers
def head(lang, title, desc, ogdesc, prefix, alt_id, alt_en):
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{ogdesc}">
<meta name="theme-color" content="#101828">
<link rel="icon" href="{prefix}assets/logo-white.svg">
<link rel="alternate" hreflang="id" href="{BASE}{alt_id}">
<link rel="alternate" hreflang="en" href="{BASE}{alt_en}">
<link rel="alternate" hreflang="x-default" href="{BASE}{alt_id}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap">
<style>{CSS}</style>
</head>
<body>
"""


def nav(lang, t, prefix, id_href, en_href, home_href):
    if lang == "id":
        sw = (f'<span aria-current="true" lang="id">ID</span>'
              f'<a href="{en_href}" hreflang="en" lang="en">EN</a>')
    else:
        sw = (f'<a href="{id_href}" hreflang="id" lang="id">ID</a>'
              f'<span aria-current="true" lang="en">EN</span>')
    return (f'<nav class="nav">\n<a href="{home_href}" aria-label="Algonova"><img src="{prefix}assets/logo-white.svg" alt="Algonova" width="120" height="32"></a>\n'
            f'<div class="nav-right"><span class="nav-tag">{t("navtag")}</span>'
            f'<div class="lang" role="navigation" aria-label="{t("langlabel")}">{sw}</div></div>\n</nav>')


def loop(prefix, name, label, w, h):
    return (f'<video class="loop" muted loop playsinline autoplay preload="none" width="{w}" height="{h}" '
            f'poster="{prefix}assets/media/{name}.jpg" aria-label="{label}">'
            f'<source src="{prefix}assets/media/{name}.mp4" type="video/mp4"></video>')


SOCIAL = [
    ("Instagram", "https://instagram.com/algonova_indonesia",
     '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true" focusable="false"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1.2" fill="currentColor" stroke="none"/></svg>'),
    ("Facebook", "https://www.facebook.com/share/1DEM9hGyvC/",
     '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="M9.101 23.691v-7.98H6.627v-3.667h2.474v-1.58c0-4.085 1.848-5.978 5.858-5.978.401 0 .955.042 1.468.103a8.68 8.68 0 0 1 1.141.195v3.325a8.623 8.623 0 0 0-.653-.036 26.805 26.805 0 0 0-.733-.009c-.707 0-1.259.096-1.675.309a1.686 1.686 0 0 0-.679.622c-.258.42-.374.995-.374 1.752v1.297h3.919l-.386 2.103-.287 1.564h-3.246v8.245C19.396 23.238 24 18.179 24 12.044c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.628 3.874 10.35 9.101 11.647Z"/></svg>'),
    ("YouTube", "https://youtube.com/@algonova_indonesia",
     '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>'),
    ("LinkedIn", "https://www.linkedin.com/company/algonova-global",
     '<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>'),
]


def footer(t, prefix):
    soc = "".join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="{n}">{ic}</a>' for n, u, ic in SOCIAL)
    return (f'<footer class="foot"><div class="wrap foot-grid">'
            f'<div class="stack" style="gap:24px"><img src="{prefix}assets/logo-white.svg" alt="Algonova" width="120" height="32">'
            f'<div class="stack" style="gap:8px"><span class="foot-h">{t("f_contact")}</span>'
            f'<a href="https://wa.me/622150996971" target="_blank" rel="noopener">WhatsApp: +62 21 50996971</a>'
            f'<a href="mailto:info@algonova.id">{t("f_email")}: info@algonova.id</a></div></div>'
            f'<div class="stack" style="gap:24px"><div class="socials">{soc}</div>'
            f'<div class="stack" style="gap:8px"><span class="foot-h">PT Algonova Indonesia Cerdas · {t("f_rights")}</span>'
            f'<a class="main" href="{t("f_main")}">algonova.com</a></div></div>'
            f'</div></footer>\n')


# ------------------------------------------------------------------ landing
def landing(lang):
    i = 0 if lang == "en" else 1
    t = lambda k: T[k][i]
    prefix = "../" if lang == "en" else ""
    meetings = "meetings/"
    wa = f"https://wa.me/{WA_NUM}?text={WA_TEXT[lang]}"
    out = [head(lang, t("title"), t("desc"), t("ogdesc"), prefix, "", "en/")]

    # HERO
    out.append(f"""<header class="hero"><div class="wrap">
{nav(lang, t, prefix, "../" if lang == "en" else "./", "en/" if lang == "id" else "./", "./")}
<div class="hero-grid">
<div class="hero-copy">
<span class="eyebrow">{t("h_eyebrow")}</span>
<h1>{t("h1a")}<br><span class="mark">{t("h1b")}</span></h1>
<p class="lead">{t("h_lead")}</p>
<div class="btns"><a class="btn btn-primary" href="#buy">{t("cta_buy")}</a><a class="btn btn-light" href="#included">{t("cta_more")}{I["arrow"](20)}</a></div>
<ul class="chips">
<li class="chip">{I["play"](18)}{t("chip1")}</li>
<li class="chip">{I["puzzle"](18)}{t("chip2")}</li>
<li class="chip">{I["screen"](18)}{t("chip3")}</li>
<li class="chip">{I["chat"](18)}{t("chip4")}</li>
</ul>
</div>
<div class="stat">
<img class="sticker" src="{prefix}assets/sticker-scratch.svg" alt="" aria-hidden="true">
<span class="muted">{t("stat_label")}</span>
<div class="num"><b>3×</b><span>{t("stat_word")}</span></div>
<span class="muted">{t("stat_sub")}</span>
</div>
</div>
</div></header>
<main>
""")

    # KEVIN (second screen): one heading, big centered video
    out.append(f"""<section id="kevin" class="sec"><div class="wrap kev">
<h2>{t("k_h2")}</h2>
<video class="kev-video" controls playsinline preload="none" width="1280" height="720" poster="{prefix}assets/media/kevin_welcome.jpg" aria-label="{t("cap_kevin")}"><source src="{prefix}assets/media/kevin_welcome.mp4" type="video/mp4"></video>
</div></section>
""")

    # INCLUDED
    arrow = I["arrow"](20)
    out.append(f"""<section id="included" class="sec bg-canvas"><div class="wrap stack" style="gap:40px">
<div class="head"><h2>{t("inc_h2")}</h2><p class="lead">{t("inc_total")}</p></div>
<div class="grid3">
<article class="card"><span class="ico">{I["play"]()}</span><h3>{t("c1t")}</h3><p>{t("c1d")}</p><a class="link" href="#more-lesson">{t("see_lesson")}{arrow}</a></article>
<article class="card on-primary"><span class="ico">{I["screen"]()}</span><h3>{t("c2t")}</h3><p>{t("c2d")}</p><a class="link" href="{meetings}">{t("all12")}{arrow}</a></article>
<article class="card"><div class="card-top"><span class="ico">{I["puzzle"]()}</span><span class="badge">{t("new")}</span></div><h3>{t("c3t")}</h3><p>{t("c3d")}</p><a class="link" href="#more-sim">{t("see_sim")}{arrow}</a></article>
<article class="card"><span class="ico">{I["chat"]()}</span><h3>{t("c4t")}</h3><p>{t("c4d")}</p><a class="link" href="#more-discord">{t("see_example")}{arrow}</a></article>
<article class="card"><span class="ico">{I["doc"]()}</span><h3>{t("c5t")}</h3><p>{t("c5d")}</p><a class="link" href="#reports">{t("see_example")}{arrow}</a></article>
<article class="card"><span class="ico">{I["trophy"]()}</span><h3>{t("c6t")}</h3><p>{t("c6d")}</p></article>
</div>
</div></section>
""")

    # HOW IT WORKS + expandable details
    chev = I["arrow"](20)

    def acc(id_, icon, title, desc, body, badge=""):
        b = f' <span class="badge">{t("new")}</span>' if badge else ""
        return (f'<details class="acc" id="{id_}"><summary><span class="ico">{icon}</span>'
                f'<span class="sm"><b>{title}{b}</b><span>{desc}</span></span>'
                f'<span class="act"><span class="o1">{t("show")}</span><span class="o2">{t("hide")}</span>{chev}</span></summary>'
                f'<div class="acc-body">{body}</div></details>')

    lesson_body = f"""<p class="muted">{t("l_lead")}</p>
<div class="parts">
<div class="part"><span class="ico">{I["play"](20)}</span><h3>{t("p1t")}</h3><p>{t("p1d")}</p></div>
<div class="part"><span class="ico">{I["quiz"](20)}</span><h3>{t("p2t")}</h3><p>{t("p2d")}</p></div>
<div class="part"><span class="ico">{I["puzzle"](20)}</span><h3>{t("p3t")}</h3><p>{t("p3d")}</p></div>
<div class="part"><span class="ico">{I["blocks"](20)}</span><h3>{t("p4t")}</h3><p>{t("p4d")}</p></div>
</div>
<div class="split">
<figure class="fig"><video controls playsinline preload="none" width="1280" height="720" poster="{prefix}assets/media/kevin_lesson.jpg"><source src="{prefix}assets/media/kevin_lesson.mp4" type="video/mp4"></video><figcaption>{t("cap_lesson")}</figcaption></figure>
<figure class="fig"><a class="zoom" href="{prefix}assets/media/course_map.jpg" target="_blank" rel="noopener" aria-label="{t("cap_map")} — {t("open_full")}"><img src="{prefix}assets/media/course_map.jpg" alt="{t("cap_map")}" width="1600" height="1375" loading="lazy"></a><figcaption>{t("cap_map")}</figcaption></figure>
</div>
"""
    sim_body = f"""<p class="muted">{t("sim_d")}</p>
<div class="grid3">
<figure class="fig">{loop(prefix, "sim_noodles_demo", t("sim1"), 960, 530)}<figcaption>{t("sim1")}</figcaption></figure>
<figure class="fig">{loop(prefix, "sim_path_demo", t("sim2"), 960, 530)}<figcaption>{t("sim2")}</figcaption></figure>
<figure class="fig">{loop(prefix, "sim_checkpoint_demo", t("sim3"), 960, 530)}<figcaption>{t("sim3")}</figcaption></figure>
</div>"""
    dc_body = f"""<div class="dc"><p class="muted">{t("dc_d")}</p>
<figure class="fig">{loop(prefix, "discord_2_tanya-tugas", t("cap_dc"), 960, 646)}<figcaption>{t("cap_dc")}</figcaption></figure></div>"""

    out.append(f"""<section id="how" class="sec"><div class="wrap stack" style="gap:40px">
<div class="head"><h2>{t("hw_h2")}</h2></div>
<div class="steps">
<article class="step"><span class="n">0</span><span class="e">{t("s0e")}</span><h3>{t("s0t")}</h3><p>{t("s0d")}</p></article>
<article class="step"><span class="n">1</span><span class="e">{t("s1e")}</span><h3>{t("s1t")}</h3><p>{t("s1d")}</p><a class="link" href="#more-lesson">{t("see_lesson")}{arrow}</a></article>
<article class="step on-primary"><span class="n">2</span><span class="e">{t("s2e")}</span><h3>{t("s2t")}</h3><p>{t("s2d")}</p><a class="link" href="{meetings}">{t("all12")}{arrow}</a></article>
<article class="step"><span class="n">3</span><span class="e">{t("s3e")}</span><h3>{t("s3t")}</h3><p>{t("s3d")}</p><a class="link" href="#reports">{t("see_example")}{arrow}</a></article>
</div>
<p class="total">{I["cal"](20)}<span>{t("repeat")}</span></p>
<div class="more">
<h3>{t("more_h3")}</h3>
{acc("more-lesson", I["play"](), t("acc_lesson_t"), t("acc_lesson_d"), lesson_body)}
{acc("more-sim", I["puzzle"](), t("c3t"), t("acc_sim_d"), sim_body, badge=True)}
{acc("more-discord", I["chat"](), t("acc_dc_t"), t("acc_dc_d"), dc_body)}
</div>
<div class="callouts">
<div class="callout warn">{I["laptop"]()}<div class="stack" style="gap:4px"><b>{t("pc_t")}</b><span>{t("pc_d")}</span></div></div>
<div class="callout role">{I["check"]()}<div class="stack" style="gap:4px"><b>{t("role_t")}</b><span>{t("role_d")}</span></div></div>
</div>
</div></section>
""")

    # REPORTS
    out.append(f"""<section id="reports" class="sec bg-canvas"><div class="wrap rep">
<div class="stack" style="gap:24px">
<div class="head"><h2>{t("r_h2")}</h2></div>
<div class="rep-items">
<div class="rep-item"><span class="ico">{I["chat"]()}</span><div class="stack" style="gap:4px"><h3>{t("r1t")}</h3><p>{t("r1d")}</p></div></div>
<div class="rep-item"><span class="ico">{I["doc"]()}</span><div class="stack" style="gap:4px"><h3>{t("r2t")}</h3><p>{t("r2d")}</p></div></div>
</div>
</div>
<div class="rep-media">
<figure class="fig"><img src="{prefix}assets/media/whatsapp_chat.jpg" alt="{t("cap_wa")}" width="600" height="833" loading="lazy"><figcaption>{t("cap_wa")}</figcaption></figure>
<figure class="fig"><a class="zoom" href="{prefix}assets/media/pdf_cycle_report.jpg" target="_blank" rel="noopener" aria-label="{t("cap_pdf")} — {t("open_full")}"><img src="{prefix}assets/media/pdf_cycle_report.jpg" alt="{t("cap_pdf")}" width="777" height="1100" loading="lazy"></a><figcaption>{t("cap_pdf")}</figcaption></figure>
</div>
</div></section>
""")

    # COMPARISON
    rows = []
    for label, reg, flex, kind in CMP:
        rl, rs = reg[i]
        fl, fs = flex[i]
        ok = f'<span class="ok" aria-hidden="true">✓</span>' if kind == "plus" else ""
        cls = "flex" + (" price" if kind == "price" else "") + (" neutral" if kind == "neutral" else "")
        ll, ls = label[i]
        rows.append(f'<tr><th scope="row"><span class="l">{ll}</span><span class="s">{ls}</span></th>'
                    f'<td class="reg"><span class="l">{rl}</span><span class="s">{rs}</span></td>'
                    f'<td class="{cls}">{ok}<span class="l">{fl}</span><span class="s">{fs}</span></td></tr>')
    out.append(f"""<section id="compare" class="sec"><div class="wrap stack" style="gap:32px">
<div class="head"><h2>{t("cmp_h2")}</h2></div>
<div class="cmp"><table>
<thead><tr><th scope="col"><span class="sr">{t("cmp_feature")}</span></th><th scope="col"><span class="l">{t("cmp_reg")}</span><span class="s">{t("cmp_reg_s")}</span></th><th scope="col" class="flex"><span class="l">{t("cmp_flex")}</span><span class="s">{t("cmp_flex_s")}</span></th></tr></thead>
<tbody>
{chr(10).join(rows)}
</tbody></table></div>
<p class="muted">{t("best")}</p>
</div></section>
""")

    # COURSE + CTA
    out.append(f"""<section class="sec" style="padding-bottom:0"><div class="wrap">
<div class="box canvas"><div class="txt"><h2>{t("about_h2")}</h2><p class="muted">{t("about_d")}</p></div>
<a class="btn btn-secondary" href="{CURRICULUM}" target="_blank" rel="noopener">{t("about_btn")}{I["arrow"](20)}</a></div>
</div></section>
<section id="buy" class="sec"><div class="wrap">
<div class="box violet"><div class="txt"><h2>{t("cta_h2")}</h2><p>{t("cta_d")}</p></div>
<a class="btn btn-wa" href="{wa}" target="_blank" rel="noopener">{I["wa"](22)}{t("cta_btn")}</a></div>
</div></section>
</main>
""")
    out.append(footer(t, prefix))
    out.append(f"<script>{JS}</script>\n</body>\n</html>\n")
    return "".join(out)


# ------------------------------------------------------------------ meetings page
def meetings(lang):
    i = 0 if lang == "en" else 1
    t = lambda k: T[k][i]
    prefix = "../../" if lang == "en" else "../"
    wa = f"https://wa.me/{WA_NUM}?text={WA_TEXT[lang]}"
    landing_href = "../"
    out = [head(lang, t("m_title"), t("m_desc"), t("m_desc"), prefix, "meetings/", "en/meetings/")]
    id_href = "../../meetings/" if lang == "en" else "./"
    en_href = "../en/meetings/" if lang == "id" else "./"
    out.append(f"""<header class="hero hero-sm"><div class="wrap">
{nav(lang, t, prefix, id_href, en_href, landing_href)}
<a class="back" href="{landing_href}">{I["back"](20)}{t("m_back")}</a>
<div class="hero-copy">
<span class="eyebrow">{t("m_eyebrow")}</span>
<h1>{t("m_h1a")} <span class="hl">{t("m_h1b")}</span></h1>
<p class="lead">{t("m_lead")}</p>
<ul class="facts"><li>{t("m_f1")}</li><li>{t("m_f2")}</li><li>{t("m_f3")}</li><li>{t("m_f4")}</li></ul>
</div>
</div></header>
<main>
<section class="sec bg-canvas"><div class="wrap stack" style="gap:32px">
<h2>{t("m_plan")}</h2>
<div class="w0"><span class="z">0</span><div class="stack" style="gap:4px"><h3>{t("m_w0t")}</h3><p>{t("m_w0d")}</p></div></div>
<div class="mods">
""")
    for mi, (mname, items) in enumerate(MODS):
        cards = []
        for c, title, desc in items:
            a, b = (c - 1) * 3 + 1, c * 3
            ruler = "".join(f'<i class="{"on" if a <= w + 1 <= b else ""}"></i>' for w in range(36))
            cards.append(f'<article class="mcard{" final" if c == 12 else ""}"><div class="row"><span class="b tnum">{c}</span>'
                         f'<span class="muted tnum">{t("m_weeks")} {a}–{b}</span></div><h3>{title[i]}</h3><p>{desc[i]}</p>'
                         f'<div class="ruler" aria-hidden="true">{ruler}</div></article>')
        out.append(f'<div class="mod"><div class="stack" style="gap:4px"><span class="m">{t("m_module")} {mi + 1}</span>'
                   f'<span class="nm">{mname[i]}</span></div><div class="mcards{" one" if len(items) == 1 else ""}">{"".join(cards)}</div></div>\n')
    segs = "".join(
        f'<div class="seg{" hot" if k == 3 else ""}" style="flex:{m[1] - m[0]}"><span class="min tnum">{m[0]}–{m[1]}</span>'
        f'<span class="t">{tt[i]}</span><span class="d">{dd[i]}</span></div>' for k, (m, tt, dd) in enumerate(EX))
    out.append(f"""</div>
<div class="panel"><div class="panel-head"><h3>{t("m_exH")}</h3><p class="muted">{t("m_exN")}</p></div>
<div><div class="bar">{segs}</div>
<div class="scale tnum" aria-hidden="true"><span>0</span><span>15</span><span>30</span><span>45</span><span>60</span><span>75</span><span>90 {t("m_min")}</span></div></div></div>
<p class="muted">{t("m_foot")}</p>
</div></section>
<section class="sec"><div class="wrap">
<div class="box violet"><div class="txt"><h2>{t("cta_h2")}</h2><p>{t("cta_d")}</p></div>
<a class="btn btn-wa" href="{wa}" target="_blank" rel="noopener">{I["wa"](22)}{t("cta_btn")}</a></div>
</div></section>
</main>
""")
    out.append(footer(t, prefix))
    out.append("</body>\n</html>\n")
    return "".join(out)


def write(rel, html):
    p = os.path.join(REPO, rel)
    os.makedirs(os.path.dirname(p) or REPO, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", rel, len(html))


write("index.html", landing("id"))
write("en/index.html", landing("en"))
write("meetings/index.html", meetings("id"))
write("en/meetings/index.html", meetings("en"))
