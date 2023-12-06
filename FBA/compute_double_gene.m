function [eg_num, growthvals, pairs] =  compute_double_gene()
    load("Ec_iJO1366.mat");
    options = optimoptions('linprog','Display','none');
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

    eg = readtable("result_single_216_egenes_found.csv");

    n = length(removeList);
    pairs = {};
    p_i=1;

    for i = 1:length(eg.(1))
        removeList{eg.(1)(i)} = [];
    end

    % build gene pairs
    for i = 1:length(removeList)
        for j = i:length(removeList)
            pairs{p_i} = [i, j];
            p_i = p_i+1;
        end
    end
    
    m = length(pairs);
    growthvals = ones(1, m);
    eg_num = 0;
    model_backup = model;

    parfor (pair_i = 1:1000,24)
        model = model_backup;
        gene_li = pairs{pair_i};
        for gene = gene_li
            rxc = removeList{gene};
            for r = rxc
                % setting corresponding bounds to 0
                model.lb(r) = 0;
                model.ub(r) = 0;
            end
        end

        % calculate new growth
        [~,g_new] = linprog(-model.c, [], [], model.S, model.b, model.lb, model.ub, options);
        growthvals(pair_i) = g_new;
        % determine if v_new is too low
        if(abs(g_new) <= abs(g_ori*0.5))
            eg_num = eg_num + 1;
            display("pairs: " + num2str() + " with growth rate "+g_new);
        end 
        if(mod(pair_i, 1000) == 0)
            display("finished " + pair_i + "/"+m);
        end
    end
    
end