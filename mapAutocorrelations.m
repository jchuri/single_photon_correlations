function [  tau, rxxs ] = mapAutocorrelations( signals, dt )
    rxxs = [];
    [rows, columns]= size(signals);
    for i=1:columns
        [tau,rxx]= autocorrelate_fft(signals(:,i),dt);
        rxxs =[rxxs (rxx * (sum(signals(:,i))^2/length(signals(:,i))))];
    end
    rxxs = rxxs(:,~all(isnan(rxxs)));
    