function [tau, rxx, standard_div, average] = calculate_g2(timeStamps, resolution, binsize)
    [t, signals] = separateIntoChunks(timeStamps, binsize, resolution);
    [tau, rxxs] = mapAutocorrelations(signals, resolution); 
    rxx = averageAndNormalize(rxx, signals);
    
    standard_div = std(rxx(10:end-10));
    average = mean(rxx(10:end-10));