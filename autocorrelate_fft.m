function [ tau, autocorrelation ] = autocorrelate_fft( signal,dt )

%signal = signal;
autocorrelation = ifft(fft(signal).*conj(fft(signal)));

% autocorrelation = autocorrelation / (mean(signal)*sum(signal));
autocorrelation = autocorrelation / (sum(signal)^2/length(signal));
% m = sum(abs(signal))./sqrt(length(signal));
% autocorrelation = 1+autocorrelation / (m^2);

tau = [dt:dt:length(signal)*dt]' - dt;

% keyboard

if nargout == 0
	plot(tau, autocorrelation, ':.k');
end
