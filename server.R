library(shiny)
users = c("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","","")
x <- c(rep(c(1:4),7))
y <- c(rep(c(1:7),4))

group1 = c('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K')
group2 = c('L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V')
group3 = c('W', 'Z', 'X', 'Y')

shinyServer(   
  function(input, output) {
   output$text1 <- renderText({
                  "A teaches a class with B, D, E, and F. C teaches 
                  a class with G, H, and I. J teaches a class with K, A, 
                  E, and G. P teaches a class with L, M, N, and O. 
                  Q teaches a class with R, S, T, U, and V. Z teaches a 
                  class with W, X, and Y. If you infect one, who else will
                  get infected?"
                  })

   output$plot <- renderPlot({
             letters <- switch(input$user,
                            "A" = group1, 
                            "B" = group1, 
                            "C" = group1, 
                            "D" = group1, 
                            "E" = group1, 
                            "F" = group1, 
                            "G" = group1, 
                            "H" = group1, 
                            "I" = group1, 
                            "J" = group2, 
                            "K" = group2, 
                            "L" = group2, 
                            "M" = group2, 
                            "N" = group2,
                            "O" = group1,
                            "P" = group1, 
                            "Q" = group2, 
                            "R" = group2, 
                            "S" = group2, 
                            "T" = group2, 
                            "U" = group2, 
                            "V" = group2, 
                            "W" = group3, 
                            "X" = group3, 
                            "Y" = group3, 
                            "Z" = group3)
             
             numberX <- switch(input$user,
                               "A" = x[1:11], 
                               "B" = x[1:11], 
                               "C" = x[1:11], 
                               "D" = x[1:11], 
                               "E" = x[1:11], 
                               "F" = x[1:11], 
                               "G" = x[1:11], 
                               "H" = x[1:11], 
                               "I" = x[1:11], 
                               "J" = x[1:11], 
                               "K" = x[1:11], 
                               "L" = x[12:22], 
                               "M" = x[12:22], 
                               "N" = x[12:22],
                               "O" = x[12:22],
                               "P" = x[12:22],
                               "Q" = x[12:22], 
                               "R" = x[12:22], 
                               "S" = x[12:22], 
                               "T" = x[12:22], 
                               "U" = x[12:22], 
                               "V" = x[12:22], 
                               "W" = x[23:26], 
                               "X" = x[23:26], 
                               "Y" = x[23:26], 
                               "Z" = x[23:26])
             
             numberY <- switch(input$user,
                               "A" = y[1:11], 
                               "B" = y[1:11], 
                               "C" = y[1:11], 
                               "D" = y[1:11], 
                               "E" = y[1:11], 
                               "F" = y[1:11], 
                               "G" = y[1:11], 
                               "H" = y[1:11], 
                               "I" = y[1:11], 
                               "J" = y[1:11], 
                               "K" = y[1:11], 
                               "L" = y[12:22], 
                               "M" = y[12:22], 
                               "N" = y[12:22],
                               "O" = y[12:22],
                               "P" = y[12:22], 
                               "Q" = y[12:22], 
                               "R" = y[12:22], 
                               "S" = y[12:22], 
                               "T" = y[12:22], 
                               "U" = y[12:22], 
                               "V" = y[12:22], 
                               "W" = y[23:26], 
                               "X" = y[23:26], 
                               "Y" = y[23:26], 
                               "Z" = y[23:26])
             
             plot(x,y,pch=users,xlab="",ylab="",
                  xlim=c(0,5),ylim=c(0,8),
                  xaxt='n',yaxt='n',cex=2.2)
             points(numberX,numberY,pch=10,col=c(input$color),cex=5)
            })
   
  }
)                                     