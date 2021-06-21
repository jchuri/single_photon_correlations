function [smoothed] = smooth_autocorrelation_curves(taus, autocorr)

time_scales = 10.^([-7:1:0; -6:1:1]);
window_size = [5 50 150 20 25 40 45 50];
smoothed = zeros(size(autocorr));

for n1=1:size(time_scales, 2)
	tmp = zeros(size(autocorr));
	inds = find(taus > time_scales(1,n1) & taus < time_scales(2, n1));
	tmp(inds) = autocorr(inds);
	%smoothed(inds) = smooth(tmp(inds), window_size(n1), 'sgolay');
	smoothed(inds) = smooth(tmp(inds), window_size(n1));
end
