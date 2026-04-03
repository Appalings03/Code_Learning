// Animation realise with https://animejs.com/
function startDiaporama(id) {
    const container = document.getElementById(id);
    const images = container.querySelectorAll('img');
    let index = 0;
    let interval;
    if (images.length <= 1) return;

    // image transition diaporama using anime.js
    const showImage = (nextIndex) => {
        anime({
            targets: images[index],
            opacity: 0,
            duration: 1000,
            easing: 'easeInOutQuad',
            complete: () => {
                images[index].classList.remove('active');
                images[nextIndex].classList.add('active');
                anime({
                    targets: images[nextIndex],
                    opacity: 1,
                    duration: 1000,
                    easing: 'easeInOutQuad'
                });
                index = nextIndex;
            }
        });
    };

    // on hover stop diaporama
    const start = () => {
        interval = setInterval(() => {
            const nextindex = (index + 1) % images.length;
            showImage(nextindex);
        }, 3000);
    };

    const stop = () => clearInterval(interval);

    // init hide all image except firt one
    images.forEach((img, i) => {
        img.style.opacity = i === 0 ? 1 : 0;
    });

    // handle stop when mouve enter or leave
    container.addEventListener('mouseenter', stop);
    container.addEventListener('mouseleave', start);

    start();
}

// contact message handling
function msg_submit() {
    const contactForm = document.getElementById('contactForm');

    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            // could do some other stuff like saving to db or sending to email
            alert(`Nom: ${name}\nEmail: ${email}`);
            contactForm.reset();
        });
    }
}

// registration handling
function registration() {
    const regis = document.getElementById('climbform');

    if (regis) {
        regis.addEventListener('submit', function(e) {
            e.preventDefault();
            const name = document.getElementById('firstname').value + ' ' + document.getElementById('lastname').value;
            const email = document.getElementById('email').value;
            const date = document.getElementById('date').value;
            const level = document.getElementById('level').value;

            alert(`Registration confirmed for ${name}\nEmail: ${email}\nDate: ${date}\nLevel: ${level}`);
            // do some other suff with checkbox to prep the gear
            regis.reset();
        });
    }
}

function btn_click() {
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('click', function () {
            alert(`You clicked on the ${button.textContent} button!`);
        });
    });
}
