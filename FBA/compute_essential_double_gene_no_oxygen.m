function [eg_num, growthvals, pairs] = compute_essential_double_gene_no_oxygen()
    load("Ec_iJO1366.mat");
    % turn off oxygen
    model.lb(252) = 0;
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

    eg = readtable("result_single_209_egenes_found_no_oxygen.csv");

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

    parfor (pair_i = 1:m,24)
        model = model_backup;
        gene_li = pairs{pair_i};
        display("what1");
        for gene = gene_li
            rxc = removeList{gene};
            for r = rxc
                % setting corresponding bounds to 0
                model.lb(r) = 0;
                model.ub(r) = 0;
            end
        end
        display("what2");

        % calculate new growth
        [~,g_new] = linprog(-model.c, [], [], model.S, model.b, model.lb, model.ub, options);
        growthvals(pair_i) = g_new;
        pairs{pair_i} = num2str(gene_li);
        display("what3");
        % determine if v_new is too low
        if(abs(g_new) <= abs(g_ori*0.5))
            eg_num = eg_num + 1;
            display("pairs: " + gene_li{1} + " " + model.genes{gene_li{1}} + " " + gene_li{2} + " " + model.genes{gene_li{2}} + " "+g_new);
        end 
        if(mod(pair_i, 1000) == 0)
            display("finished " + pair_i + "/"+m);
        end
    end


end