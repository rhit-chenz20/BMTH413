
% single gene knockout
% [indexes, ids, num] = computation_essential_gene(0);
% filename = "result_single_" + num + "_egenes_found.csv";
% name = string(indexes).';
% T = table(ids.', 'RowNames',name);
% writetable(T,filename,'WriteRowNames',true);  

% double gene knockout
[eg_num, growthvals, pairs] = compute_double_gene();
filename = "result_double_" + eg_num + "_pairs_found.csv";
name = string(pairs).';
T = table(growthvals.', 'RowNames',name);
writetable(T,filename,'WriteRowNames',true);

