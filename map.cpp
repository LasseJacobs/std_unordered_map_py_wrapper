
#include <string>
#include <unordered_map>

namespace pw
{
    template<typename T>
    struct result
    {
        T value;
        bool found;
    };
    
    typedef unsigned int size_type;
}

namespace ds 
{
    typedef std::unordered_map<std::string, std::string> map;
    typedef pw::result<const char*> result; 
}

extern "C" 
{
    /*
     * Constructors 
     */
     
    ds::map* new_map() 
    { 
        return new ds::map(); 
    }
    
    
    /*
     * Capacity 
     */
     
    bool m_empty(const ds::map* map)
    {
        return map->empty();
    }
    
    pw::size_type m_size(const ds::map* map)
    {
        return map->size();
    }
    
    pw::size_type m_max_size(const ds::map* map)
    {
        return map->max_size();
    }
    
    
    /*
     * Modifiers 
     */
     
    void m_clear(ds::map* map) 
    { 
        map->clear();
    }
    
    void m_set(ds::map* map, const char* key, const char* value) 
    {
        (*map)[key] = value;
    }
    
    void m_erase(ds::map* map, const char* key) 
    { 
        map->erase(key);
    }
    
    void m_swap(ds::map* map, ds::map* other)
    {
        map->swap(*other);
    }
    
    
    /*
     * Lookup 
     */
     
    // at -> look up how to implement exceptions
     
    const char* m_get(const ds::map* map, const char* key) 
    {
        // operator[] -> check what happens when non-existing access 
        auto itr = map->find(key);
        if(itr == map->end())
            return nullptr;
            
        return itr->second.c_str();
    }
    
    pw::size_type m_count(const ds::map* map, const char* key) 
    {
        map->count(key);
    }
    
    ds::result m_find(const ds::map* map, const char* key)
    {
        auto itr = map->find(key);
        if(itr == map->end())
            return {"", false};
            
        return {itr->second.c_str(), true};
    }
    
    
    /*
     * Bucket interface 
     */
     
    pw::size_type m_bucket_count(const ds::map* map)
    {
        return map->bucket_count();
    }
    
    pw::size_type m_max_bucket_count(const ds::map* map)
    {
        return map->max_bucket_count();
    }
    
    pw::size_type m_bucket_size(const ds::map* map, pw::size_type n)
    {
        return map->bucket_size(n);
    }
    
    pw::size_type m_bucket(const ds::map* map, const char* key)
    {
        return map->bucket(key);
    }
    
        
    /*
     * Hash Policy 
     */
    
    float m_load_factor(const ds::map* map)
    {
        return map->load_factor();
    }
    
    float m_get_max_load_factor(const ds::map* map)
    {
        return map->max_load_factor();
    }
    
    void m_set_max_load_factor(ds::map* map, float ml)
    {
        map->max_load_factor(ml);
    }
    
    void m_rehash(ds::map* map, pw::size_type count)
    {
        return map->rehash(count);
    }
    
    void m_reserve(ds::map* map, pw::size_type count)
    {
        return map->reserve(count);
    }
    
        
    /*
     * Destructor 
     */
    
    void delete_map(ds::map* map) 
    { 
        delete map;
    }
}
