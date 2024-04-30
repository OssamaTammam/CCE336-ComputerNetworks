import dns.resolver

# Step 4: Determine the authoritative name server for the iit.ac.in domain
domain = "iitb.ac.in"
resolver = dns.resolver.Resolver()
try:
    ns_records = resolver.query(domain, "NS")
    # If there are multiple authoritative servers, get the name of the first one
    first_authoritative_server = str(ns_records[0])
    print(
        "The name of the authoritative name server for",
        domain,
        "is:",
        first_authoritative_server,
    )

    # Step 5: Find the IP address of the authoritative name server
    authoritative_ip = resolver.query(first_authoritative_server)
    print(
        "The IP address of the authoritative name server",
        first_authoritative_server,
        "is:",
        authoritative_ip[0],
    )

except dns.resolver.NoAnswer:
    print("No authoritative name servers found for", domain)
except dns.resolver.NXDOMAIN:
    print("Domain", domain, "does not exist")
except dns.exception.Timeout:
    print("DNS query timed out")
