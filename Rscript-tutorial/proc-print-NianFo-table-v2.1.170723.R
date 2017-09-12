
  NianFo_tab <- t(NianFo_tab)
  n <- ncol(NianFo_tab)

  # n.col <- 10
  m <- n %% n.col
  m <- ifelse(m == 0, 0, n.col - m)
  NianFo_tab_new <- cbind(NianFo_tab, matrix("", nrow = nrow(NianFo_tab), ncol = m) )


  m <- ncol(NianFo_tab_new) %/% n.col
  mx <- NULL
  for(i in 1:m){
    col.idx <- ( (i-1)*n.col + 1 )  : ( i*n.col )
    mx <- rbind(mx, NianFo_tab_new[, col.idx])
  }
  colnames(mx) <- 1:n.col

  tspanner.names <- rep(NA, m)
  for(i in 1:(m-1)){
    start.idx <- (i-1)*n.col + 1
    end.idx <- i*n.col
    tspanner.names[i] <- paste('第', start.idx, '~', end.idx , '个团体', sep='' )
  }
  if( (n-1) %% n.col == 0 ){
    tspanner.names[m] <- '合计'
  }else if( (n-1) %% n.col == 1 ){
    tspanner.names[m] <- paste('第', (n-1), '个团体及合计', sep='' )
  }else{
    tspanner.names[m] <- paste('第',  (m-1)*n.col + 1, '~', n-1,  '个团体及合计', sep='' )
  }

  # htmlTable::htmlTable(mx,
  #                      col.rgroup = c("#F7F7F7", "none"),
  #                      tspanner = tspanner.names,
  #                      n.tspanner = rep(5, m),
  #                      ## padding to cells: top side bottom
  #                      css.cell = 'padding: 0px 5px 0px;'
  # )
