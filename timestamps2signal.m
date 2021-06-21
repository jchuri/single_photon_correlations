function [dt, signal] = timestamps2signal(timestamps, bin_time)

clk_time = 20e-9;
time_ratio = clk_time / bin_time;

dt = bin_time;
shift = timestamps(1);
timestamps = round((timestamps - shift) .* time_ratio)+1;
signal = zeros(timestamps(end), 1);


for i = timestamps
    signal(i) = 1;
end
