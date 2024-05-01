start();
date();

    // Get information and play song
    function getSongId(audio) {
        var nameMusic = document.getElementById('nameMusic');
        var imageMusic = document.getElementById('imageMusic');
        var artistMusic = document.getElementById('artistMusic');
        const music = audio.split(",");
        // var loadingId = "loading_" + music[1];
        // var loading = document.getElementById(loadingId);
        // var playId = "play_" + music[1];
        // var playElement = document.getElementById(playId);


        // loading.innerHTML = `<div class="load"></div>
        //       <div class="load"></div>
        //       <div class="load"></div>
        //       <div class="load"></div>` 
        // playElement.removeAttribute("class")
        
          nameMusic.innerHTML = music[1];
          imageMusic.src = music[2];
          artistMusic.innerHTML = music[3];
          loadMusic(music[0]);
          

      };
    
    // Load music
    function loadMusic(audio_privew) {
          var audio = document.getElementById('myAudio');
          var playPauseBtn = document.getElementById('play_pause_btn');
          
          audio.src = audio_privew;
          audio.play();


          playPauseBtn.innerHTML = '<i class="fa-solid fa-pause"></i>';
          if (audio.ended){
            playElement.classList.add("play");
            }
      };

    //  Start app
    function start() {
        var audio = document.getElementById('myAudio');
        var currentTimeDisplay = document.getElementById('currentTime');
        var timeEndDisplay = document.getElementById('timeEnd');
        var progressBar = document.getElementById('progressBar');
        var volumeControl = document.getElementById('volumeControl');
        var playPauseBtn = document.getElementById('play_pause_btn');
        var volumeIcon = document.getElementById('volume_icon');
        var volumeMusic = 100;

    
        audio.addEventListener('timeupdate', function () {
            var currentTime = audio.currentTime;
            var duration = audio.duration;
            
            var progressPercentage = (currentTime / duration) * 100;
            progressBar.value = progressPercentage;
    
            var minutes = Math.floor(currentTime / 60);
            var seconds = Math.floor(currentTime % 60);
            var timeString = (minutes) + ':' + padZero(seconds);
            currentTimeDisplay.innerHTML = timeString;

            var minutes = Math.floor(duration / 60);
            var seconds = Math.floor(duration % 60);
            var timeEndStrings = (minutes) + ':' + padZero(seconds);

            if (audio.ended){
              playPauseBtn.innerHTML = '<i class="fa-solid fa-play"></i>';
            }
            timeEndDisplay.innerHTML = timeEndStrings
            
        });

        playPauseBtn.addEventListener('click', function () {
            if (audio.paused) {
                audio.play();
                playPauseBtn.innerHTML = '<i class="fa-solid fa-pause"></i>'; // Pause icon
            }
            else{
                audio.pause();
                playPauseBtn.innerHTML = '<i class="fa-solid fa-play"></i>'; // Play icon
                
            }
        });
    
        progressBar.addEventListener('input', function () {
            var seekTime = (progressBar.value / 100) * audio.duration;
            audio.currentTime = seekTime;
        });
        
    
        volumeControl.addEventListener('input', function () {
            audio.volume = volumeControl.value / 100;
        });

        volumeIcon.addEventListener('click', function(){
          
          if (volumeControl.value != 0){
            volumeMusic = volumeControl.value
          }
          // Kiểm tra nếu âm thanh đã được tắt
          if (volumeControl.muted) {
              // Bật âm thanh trở lại
              volumeControl.muted = false;
              console.log(volumeMusic);
              volumeControl.value = volumeMusic;
              audio.volume = volumeControl.value / 100;
              volumeIcon.innerHTML = '<i class="fa-solid fa-volume-high"></i>';
          } else {
              // Tắt âm thanh
              volumeControl.muted = true; 
              audio.volume = 0;
              volumeControl.value = 0;
              volumeIcon.innerHTML = '<i class="fa-solid fa-volume-mute"></i>';
          }
          
        });
    
        function padZero(number) {
            return (number < 10 ? '0' : '') + number;
        }

    };
    function date(){
        var divElements = document.getElementsByClassName("date_ct");
        moment.locale('vi');
        var noiDung;
        var ngayHienTai = moment();
        var ngayFortmat;
        
        for (var i = 0; i < divElements.length; i++) {
            noiDung = divElements[i].innerHTML;
            
        
            ngayHienTai = moment(noiDung)
            ngayFortmat = ngayHienTai.subtract('day').fromNow();
            divElements[i].innerHTML = ngayFortmat
        }
    }

    