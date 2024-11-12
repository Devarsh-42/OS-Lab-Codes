n = int(input("Enter the number of page frames: "))
N = int(input("Enter the number of reference strings: "))

a = list(map(int, input("Enter the reference string (space-separated): ").split()))
pfr = []
pfa = 0
ph = 0

for i in range(N):
    page = a[i]
    print(f"Accessing page {page}:")

    if page in pfr:
        ph += 1
        print(f"Page {page} already in frames {pfr} (Page Hit)")
        continue  

    if len(pfr) < n:
        pfr.append(page)
        pfa += 1
        print(f"Page {page} added to frames: {pfr} (Page Fault)")
    else:

        farthest_index = -1
        farthest_page = -1

        for p in pfr:
            
            try:
                index = a.index(p, i + 1)
            except ValueError:
                
                farthest_page = p
                break

            if index > farthest_index:
                farthest_index = index
                farthest_page = p

        pfr[pfr.index(farthest_page)] = page
        pfa += 1
        print(f"Page {page} replaced {farthest_page}. New frames: {pfr} (Page Fault)")

print(f"Total Page Hits: {ph}")
print(f"Total Page Faults: {pfa}")
print(f"Hit Ratio: {(ph / N):.2f}")
