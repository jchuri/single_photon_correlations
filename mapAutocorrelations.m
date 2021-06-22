function [  tau, rxxs ] = mapAutocorrelations( signals, dt )
    rxxs = [];
    [rows, columns]= size(signals);
    for i=1:columns
        [tau,rxx]= autocorrelate_fft(signals(:,i),dt);
        rxxs =[rxxs rxx];
    end
    rxxs = rxxs(:,~all(isnan(rxxs)));
    