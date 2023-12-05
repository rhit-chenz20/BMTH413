[indexes, ids, num] = computation_essential_gene(1);
filename = "result_" + num + "_egenes_found.csv";
rownames = {'gene indexes';'gene ids'};
T = table(indexes,ids, 'RowNames',rownames);
writetable(T,filename,'WriteRowNames',true);  
