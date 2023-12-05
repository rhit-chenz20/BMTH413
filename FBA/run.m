
% single gene knockout
% [indexes, ids, num] = computation_essential_gene(0);
% filename = "result_single_" + num + "_egenes_found.csv";
% name = string(indexes).';
% T = table(ids.', 'RowNames',name);
% writetable(T,filename,'WriteRowNames',true);  

% double gene knockout
[indexes, ids, num] = computation_essential_gene(1);
filename = "result_double_" + num + "_egenes_found.csv";
name = string(indexes).';
T = table(ids.', 'RowNames',name);
writetable(T,filename,'WriteRowNames',true);  
