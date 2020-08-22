clc;
clear;
= audiorecorder(22050,8,1); 
disp('Inicie a hablar'); %iniciamos a hablar
recordblocking(voice, 20); %cantidad de segundos hablando
disp('Termine de hablar'); %
voz = getaudiodata(voice); %guardamos la senal de voz codificada
welchfunc=pwelch(voz);
plot(welchfunc);
title('PSD de mi voz durante 5 segundos')
xlabel('Frecuencia [Hz]')
ylabel('Vatios por Hert [W/Hz]')
