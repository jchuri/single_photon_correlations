function [ dt, signals] = separateIntoChunks(timestamps, segmentTime,samplingTime)
    [t,I] = timestamps2signal(timestamps,samplingTime);
    dt = samplingTime;
    signals = [];
    cutOff = round(1.1*segmentTime/samplingTime);
    for i=1:round(segmentTime/samplingTime):length(I)-cutOff
        signals= [signals I(i:i+cutOff)];
    end