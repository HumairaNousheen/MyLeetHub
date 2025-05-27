class Solution(object):
    def floodFill(self, image, sr, sc, color):
        # you can either do DFS (go deep and backtrack) or BFS (use q to color level wise)
        row,col=len(image),len(image[0])
        if image[sr][sc]==color:
            return image #no more work needed
        original_color=image[sr][sc]  

        def BFS(r,c,color,original_color,image):
            q=[(r,c)]   
            while q:
                # pop that element
                pixel=q.pop(0) #(r,c)
                #color that pixel
                r,c=pixel
                image[r][c]=color
                # now append top,bottom,left,right to q only if they are within bound and equal to original color

                #append up [r-1][c]
                new_r,new_c=r-1,c
                if (new_r>=0 and new_r<row) and (0 <= new_c < col) and image[new_r][new_c]==original_color:
                    q.append((new_r,new_c))
                #append down [r+1][c]
                new_r,new_c=r+1,c
                if (new_r>=0 and new_r<row) and (0 <= new_c < col) and image[new_r][new_c]==original_color:
                    q.append((new_r,new_c))
                #append left [r][c-1]
                new_r,new_c=r,c-1
                if (new_r>=0 and new_r<row)  and (0 <= new_c < col) and image[new_r][new_c]==original_color:
                    q.append((new_r,new_c))
                #append right [r][c+1]
                new_r,new_c=r,c+1
                if (new_r>=0 and new_r<row) and (0 <= new_c < col)  and image[new_r][new_c]==original_color:
                    q.append((new_r,new_c))

            return image    
        
        ans=BFS(sr,sc,color,original_color,image)
        return ans

          
