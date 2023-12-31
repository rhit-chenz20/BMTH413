function [eg_index, eg_id, eg_num] = computation_essential_gene()
    load("Ec_iJO1366.mat");
    eg_index = [];
    eg_id = [];
    eg_num = 0;
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

        % if double gene knockout is enabled
        if(double_gene_knockout == 1)
            parfor gene_i_2 = 1:length(removeList)
                model = model_backup;
                rxcs_2 = removeList{gene_i_2};
                for rxc_i_2 = 1:length(rxcs_2)
                    rxc_index_2 = rxcs_2(rxc_i_2);
                    % setting corresponding bounds to 0
                    model.lb(rxc_index_2) = 0;
                    model.ub(rxc_index_2) = 0;
                end
                % calculate new growth
                [~,g_new] = linprog(-model.c, [], [], model.S, model.b, model.lb, model.ub, options);
                % determine if v_new is too low
                if(abs(g_new) <= abs(g_ori*0.5))
                    display("gene1 index: " + gene_i);
                    display("gene2 index: " + gene_i_2);
                    eg_index{gene_i,gene_i_2} = string(gene_i) + " " + string(gene_i_2);
                    
                end 
                % if(mod(gene_i, 10) == 0)
                %     display("not dead, yet");
                % end
                % restore model
                
            end
            num = num + 1;
            display(num + " gene done");
        else
            % calculate new growth
            [~,g_new] = linprog(-model.c, [], [], model.S, model.b, model.lb, model.ub, options);
     
            % determine if v_new is too low
            if(abs(g_new) <= abs(g_ori*0.5))
                eg_index{essential_genes_i} = gene_i;
                eg_id{essential_genes_i} = model.genes{gene_i};
                essential_genes_i = essential_genes_i + 1;
            end 
            if(mod(gene_i, 100) == 0)
                display("not dead, yet");
            end
            % restore model
            model = model_backup;
        end
    end

    
    
    eg_num = length(eg_index);
    % fprintf("%d essential genes are found", length(eg_index));
end