document.addEventListener('DOMContentLoaded', () => {
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    let room = 'Default';
    joinRoom(room);

    //make the enter key send the message
    document.querySelector('#ConversationInput').addEventListener("keyup", function(event) {
        if (event.keyCode === 13) {
            event.preventDefault();
            document.querySelector('#BtnSend').click();
        }
    });

    socket.on('connect', () => {
        socket.send("I am connected"); // Send msg to the default event handler "bucket" in the server called message
    });

    // socket.on('message', data => {
    //     console.log(`Message received: ${data}`);
    // });

    socket.on('message', data => {
        uName = data['user'];
        msg = data['msg'];
        time = data['time'];

        console.log(`Message received: ${msg}`);
        console.log(`User: ${uName}`);

        // Create the list item element
        const listItem = document.createElement('li');
        listItem.classList.add('clear-both', 'py-4');

        // Create the inner container div
        const innerContainer = document.createElement('div');
        innerContainer.classList.add('relative', 'inline-flex', 'items-end', 'mb-6', 'text-right', 'ltr:rtl:float-left', 'ltr:float-right', 'rtl:float-left');

        // Create the user avatar div
        const userAvatar = document.createElement('div');
        userAvatar.classList.add('order-3', 'mr-0', 'ltr:ml-4', 'rtl:mr-4');

        // Create the user avatar image
        const avatarImage = document.createElement('img');
        avatarImage.setAttribute('src', 'assets/images/avatar-1.jpg');
        avatarImage.setAttribute('alt', '');

        // Append the avatar image to the user avatar div
        userAvatar.appendChild(avatarImage);

        // Create the main content div
        const mainContent = document.createElement('div');

        // Create the content div for the message
        const messageContent = document.createElement('div');
        messageContent.classList.add('relative', 'order-2', 'px-5', 'py-3', 'text-gray-700', 'rounded-lg', 'ltr:rounded-br-none', 'rtl:rounded-bl-none', 'bg-gray-50', 'dark:bg-zinc-700', 'dark:text-gray-50');

        // Create the message paragraph
        const messageParagraph = document.createElement('p');
        messageParagraph.textContent = msg;

        // Create the time paragraph
        const timeParagraph = document.createElement('p');
        timeParagraph.textContent = time;
        timeParagraph.classList.add('mt-1', 'text-xs', 'text-left', 'text-gray-500', 'dark:text-gray-300');

        // Append the message and time paragraphs to the message content div
        messageContent.appendChild(messageParagraph);
        messageContent.appendChild(timeParagraph);

        // Create the before content div (triangle shape)
        const beforeContent = document.createElement('div');
        beforeContent.classList.add('before:content-[""]', 'before:absolute', 'before:border-[5px]', 'before:border-transparent', 'ltr:before:border-r-gray-50', 'ltr:before:border-t-gray-50', 'rtl:before:border-l-gray-50', 'rtl:before:border-t-gray-50', 'ltr:before:right-0', 'rtl:before:left-0', 'before:-bottom-2', 'ltr:dark:before:border-t-zinc-700', 'ltr:dark:before:border-r-zinc-700', 'rtl:dark:before:border-t-zinc-700', 'rtl:dark:before:border-l-zinc-700');

        // Append the message content and before content to the main content div
        mainContent.appendChild(messageContent);
        mainContent.appendChild(beforeContent);

        // Create the dropdown div
        const dropdownDiv = document.createElement('div');
        dropdownDiv.classList.add('relative', 'self-start', 'order-1', 'dropdown');

        // Create the dropdown toggle link
        const dropdownToggle = document.createElement('a');
        dropdownToggle.classList.add('p-0', 'text-gray-400', 'border-0', 'btn', 'dropdown-toggle', 'dark:text-gray-100');
        dropdownToggle.setAttribute('href', '#');
        dropdownToggle.setAttribute('role', 'button');
        dropdownToggle.setAttribute('data-bs-toggle', 'dropdown');
        dropdownToggle.setAttribute('id', 'dropdownMenuButton16');

        // Create the dropdown menu
        const dropdownMenu = document.createElement('div');
        dropdownMenu.classList.add('absolute', 'z-50', 'hidden', 'py-2', 'my-6', 'text-left', 'list-none', 'bg-white', 'border-none', 'rounded', 'shadow-lg', 'ltr:right-auto', 'ltr:left-0', 'xl:ltr:right-0', 'xl:ltr:left-auto', 'rtl:right-0', 'rtl:left-auto', 'xl:rtl:left-0', 'xl:rtl:right-auto', 'dropdown-menu', 'w-36', 'bg-clip-padding', 'dark:bg-zinc-700');
        dropdownMenu.setAttribute('aria-labelledby', 'dropdownMenuButton16');

        // Create dropdown items
        const dropdownItems = [
          { text: 'Copy', icon: 'ri-file-copy-line' },
          { text: 'Save', icon: 'ri-save-line' },
          { text: 'Forward', icon: 'ri-chat-forward-line' },
          { text: 'Delete', icon: 'ri-delete-bin-line' },
        ];

        // Create and append dropdown items
        dropdownItems.forEach((item) => {
          const dropdownItem = document.createElement('a');
          dropdownItem.classList.add('block', 'w-full', 'px-4', 'py-2', 'text-sm', 'font-normal', 'text-gray-700', 'bg-transparent', 'dropdown-item', 'whitespace-nowrap', 'hover:bg-gray-100/50', 'dark:text-gray-100', 'dark:hover:bg-zinc-600', 'ltr:text-left', 'rtl:text-right');
          dropdownItem.textContent = item.text;

          const icon = document.createElement('i');
          icon.classList.add('text-gray-500', 'rtl:float-left', 'ltr:float-right', 'dark:text-gray-200', item.icon);

          dropdownItem.appendChild(icon);
          dropdownMenu.appendChild(dropdownItem);
        });

        // Append the dropdown toggle and menu to the dropdown div
        dropdownDiv.appendChild(dropdownToggle);
        dropdownDiv.appendChild(dropdownMenu);

        // Create the user name div
        const userNameDiv = document.createElement('div');
        userNameDiv.classList.add('font-medium', 'text-gray-700', 'rtl:text-left', 'text-14', 'dark:text-gray-300');
        userNameDiv.textContent = uName;

        // Append all the elements to the main content div
        mainContent.appendChild(userNameDiv);
        mainContent.appendChild(dropdownDiv);

        // Append the inner container div to the list item
        innerContainer.appendChild(userAvatar);
        innerContainer.appendChild(mainContent);

        // Append the inner container div to the list item
        listItem.appendChild(innerContainer);

        // Append the list item to your list container
        const listContainer = document.getElementById('MainConversation');
        listContainer.appendChild(listItem);
    });

    socket.on('smtg', data => {
        console.log(`Message received: ${data}`);
    });

    document.querySelector('#BtnSend').onclick = () => {
        text = document.querySelector('#ConversationInput').value;
        if (text == '') {
            return false;
        }
        socket.send({'msg': text, 'user': username, 'room': room});

        document.querySelector('#ConversationInput').value = '';

    };

    document.querySelectorAll(".RoomSelection").forEach(a => {
        a.onclick = () => {
            let h5Text = a.querySelector('h5').textContent;
            let newRoom = h5Text.substring(1);
             console.log(newRoom);
            if (newRoom == room) {
                msg = `You are already in ${room} room`;
                printSysMsg(msg);
            } else {
                if(room == 'None'){
                    joinRoom(newRoom);
                    room = newRoom;
                }
                else {
                leaveRoom(room);
                joinRoom(newRoom);
                room = newRoom;
                }
            }
            console.log(a);
            console.log(newRoom);

        };
    });

    function leaveRoom(room) {
        socket.emit('leave', {'username': username, 'room': room});
    }

    function joinRoom(room) {
        socket.emit('join', {'username': username, 'room': room});
        document.querySelector('#ConversationInput').focus();
    }

    function printSysMsg(msg) {
        const listItem = document.createElement('li');
        listItem.classList.add('text-center', 'text-gray-500', 'text-xs', 'py-2');
        listItem.innerHTML = msg;
        document.querySelector('#MainConversation').append(listItem);
    }






});