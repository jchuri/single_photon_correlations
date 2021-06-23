function rxx = averageAndNormalize(rxxs, signals)
    % Remove NaNs
    signals = signals(:, ~all(isnan(rxxs)));
    rxxs = rxxs(:, ~all(isnan(rxxs)));

    % Average Normalization
    T = length(signals(:,1));
    N_c = sum(mean(signals,2));
    rxx = mean(rxxs,2) / (N_c^2 / T);