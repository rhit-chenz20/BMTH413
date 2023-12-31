function [eg_index, eg_id, eg_num] = compute_essential_gene_no_oxygen()
    load("Ec_iJO1366.mat");
    eg_index = [];
    eg_id = [];
    eg_num = 0;
    % turn off oxygen
    model.lb(252) = 0;
    options = optimoptions('linprog','Display','none');
    % old growth rate
    [~,g_ori] = linprog(-model.c, [], [], model.S, model.b, model.lb, model.ub, options);
    
    % identify reaction
    for numGene = 1:length(model.genes)
       geneVector = [numGene];
       rxnList = [];
       for i=1:length(geneVector)
          rxnList = union(rxnList,find(model.rxnGeneMat(:,geneVector(i))==1));
       end
       rxnList = sort(rxnList);
       if (~isempty(rxnList))
          x = true(size(model.genes));
          x(geneVector) = false;
          removeList{numGene} = [];
          for i = 1:length(rxnList)
             if (~eval(model.rules{rxnList(i)}))
                removeList{numGene} = union(removeList{numGene},rxnList(i));
             end
          end
       end
    end
    
    
    model_backup = model;
    essential_genes_i = 1;
    eg_index = [];
    
    % disable reactions by changing bounds to 0
    num = 0;
    % looping through all genes
    for gene_i = 1:length(removeList)
        % for each gene at model.gene{gene_i}, get the list of reactions it affects
        % removeList{i}: list of indexes of reactions affected by gene at model.genes{gene_i}
        rxcs = removeList{gene_i};
    
        % loop through all the reacions model.genes{gene_i} affects
        for rxc_i = 1:length(rxcs)
            rxc_index = rxcs(rxc_i);
            % setting corresponding bounds to 0
            model.lb(rxc_index) = 0;
            model.ub(rxc_index) = 0;
        end
        % calculate new growth
        [~,g_new] = linprog(-model.c, [], [], model.S, model.b, model.lb, model.ub, options);
 
        % determine if v_new is too low
        if(abs(g_new) <= abs(g_ori*0.5))
            eg_index{essential_genes_i} = gene_i;
            eg_id{essential_genes_i} = model.genes{gene_i};
            essential_genes_i = essential_genes_i + 1;
            display("essential gene: " + gene_i + " " + model.genes{gene_i} + " "+g_new);
        end 
        if(mod(gene_i, 100) == 0)
            display("not dead, yet");
        end
        % restore model
        model = model_backup;
    end
    eg_num = length(eg_index);
    fprintf("%d essential genes are found", length(eg_index));
end